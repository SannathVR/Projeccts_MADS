
clear;
close all;

load('C:\Users\Sannath\OneDrive\Documents\Visual Studio 2015\Desktop\D_bc_tr.mat');
load('C:\Users\Sannath\OneDrive\Documents\Visual Studio 2015\Desktop\D_bc_te.mat');

PLOT = 1 ;

dim = 30;
K = 13 ;

train = zeros(30,480);
for i = 1:30
    x = D_bc_tr(i,:);
    m = mean(x);
    v = sqrt(var(x));
    train(i, : ) = (x-m)/v;
end

test =zeros(30,89);
for i = 1:30
    x = D_bc_te(i,:);
    m = mean(x);
    v = sqrt(var(x));
    test(i, :) = (x - m)/v;
end

y_train = D_bc_tr(31,:);
y_test = D_bc_te(31,:);

D_train = [train; y_train];
D_test = [test; y_test];


eps = 10^-9;
W = zeros(dim+1,1);

h = zeros(1,K);
k=1;

gk = g_wdbc(W, D_train);
dir = -gk;

alpha_k = bt_lsearch(W,dir,'f_wdbc','g_wdbc', D_train);

while(norm(alpha_k*dir) >=eps && (k<K))

    W = W +alpha_k*dir;
    gk = g_wdbc(W,D_train);
    dir = -gk;
    alpha_k = bt_lsearch(W,dir,'f_wdbc','g_wdbc',D_train);
    h(k) = f_wdbc(W,D_train);
    k=k+1;
   
end

Dt = [test; ones(1,89)];
Result = W'*Dt;
TestLabel = zeros(1,length(Result));
FalsePos = 0
FalseNeg = 0 ;

for ii = 1:length(Result)
    if Result(ii)<0
        TestLabel(ii) = -1;
        if y_test(ii) > 0
            FalseNeg = FalseNeg + 1;
        end
    else
        TestLable(ii) = 1;
        if y_test(ii) < 0
            FalsePos = FalsePos + 1;
        end
    end 
end


error_percent = (FalsePos/89)*100;
accuracy = 100-error_percent;
fprintf('\t\t Logistic Regression Results for  Breast Cancer Test Dataset \n\ntotal instances : 89\n')
fprintf('mis-classifications : %d\n', FalsePos)
fprintf('error : %2.4f%% \n', error_percent)
fprintf('accuracy: %2.4f%% \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', accuracy)





