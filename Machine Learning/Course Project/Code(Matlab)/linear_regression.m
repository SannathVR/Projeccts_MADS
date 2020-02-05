clc
close all

load('C:\Users\Sannath\OneDrive\Documents\Visual Studio 2015\Desktop\D_bc_tr.mat');
load('C:\Users\Sannath\OneDrive\Documents\Visual Studio 2015\Desktop\D_bc_te.mat');


Benign = [];
Malignant = [];

for i = 1 : 480

    if D_bc_tr(31,i) == -1

        b = D_bc_tr(:,i);
        Benign = [Benign b];

end

if D_bc_tr(31,i) == 1

    m = D_bc_tr(:,i);
    Malignant = [Malignant m];

end

end

x1 = Benign(1:30,:);
x2 = Malignant(1:30,:);
y1 = [ones(300,1);-ones(180,1)];
y2 = [ones(180,1);-ones(300,1)];

%Xtr = [Xtr1 Xtr2];
x1_A = [x1 x2];
x1_A(31,:) = [ones(1,300) ones(1,180)];

inv = x1_A'; 
w1_vec = pinv(inv)*y1;
w1 = w1_vec(1:30,:);
b1 = w1_vec(31,:);

x2_A = [x2 x1];
x2_A(31,:) = [ones(1,180) ones(1,300)];

inv = x2_A'; 
w2_vec = pinv(inv)*y2;
w2 = w2_vec(1:30,:);
b2 = w2_vec(31,:);

weight = [w1 w2];
bias = [b1;b2];

Label = D_bc_te(31,:);

L_1 = [];
L_2 = [];
test1 = [];
test2 = [];

for i = 1 : 89

    if Label(:,i) == -1

        l2  = -1;
        L_2 = [L_2 l2];
        test = D_bc_te(1:30,i);
        test1 = [test1 test];

    end

    if Label(:,i) == 1

        l1  = 1;
        L_1 = [L_1 l1];
        test = D_bc_te(1:30,i);
        test2 = [test2 test];

    end

end

L = [L_1 L_2];
XTe = [test1 test2];

test = [XTe];
Label = [ones(1,57) ones(1,32)+1];

ek = zeros(2,89);
predict_wrong = 0;

for col = 1:89

    f = weight'*test(:,col)+bias;
    [maxvalue index] = max(f);
    ek(index,col)  = 1;

    if index ~= Label(col)

        predict_wrong = predict_wrong +1;

    else

    end

end


ek;
predict_wrong;

error_percent = predict_wrong/89*100;
accuracy = 100 - error_percent;


fprintf('\t\tLinear Model Results for  Breast Cancer Test Dataset \n\ntotal instances : 89\n')
fprintf('mis-classifications : %d\n', predict_wrong)
fprintf('error : %2.4f%% \n', error_percent)
fprintf('accuracy: %2.4f%% \n\n', accuracy)
