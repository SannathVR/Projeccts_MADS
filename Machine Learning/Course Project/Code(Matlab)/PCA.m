clc
close all

load('C:\Users\Sannath\OneDrive\Documents\Visual Studio 2015\Desktop\D_bc_tr.mat');
load('C:\Users\Sannath\OneDrive\Documents\Visual Studio 2015\Desktop\D_bc_te.mat');

Benign = [];
Malignant = [];

for i = 1 : 480
    
    if D_bc_tr(31,i) == 1

        b = D_bc_tr(:,i);
        Benign = [Benign b];

    end

    if D_bc_tr(31,i) == -1

        m = D_bc_tr(:,i);
        Malignant = [Malignant m];

    end

end

X = [Benign(1:30,:) Malignant(1:30,:)];

d = 48;
q = 8;
m1 = [];
u = [];

m2 = [];
u1 = [];

m3 = [];
u2 = [];

for j = 0 : 1

if j == 0

d = 180;
X1 = X(:,1:180);
m = mean(X1,2);
A = X1 - m;
C = 1/d*(A*A');

[uq, S] = eigs(C,q);
m2 = [m2 m];
u1 = [u1 uq];

end

if j == 1

d = 300;
X1 = X(:,181:end);
m = mean(X1,2);
A = X1 - m;
C = 1/d*(A*A');

[uq, S] = eigs(C,q);
m3 = [m3 m];
u2 = [u2 uq];

end	
end

u = [u1 u2];
m1 = [m2 m3];
test_bc = D_bc_te(1:30,:);

for j = 1:89
for i = 0:1

Uq = u(:,(i*q)+1:(i+1)*q);
f_j = Uq'*(test_bc(:,j)-m1(:,i+1));
x_vec = Uq*f_j+m1(:,i+1);
nrm(i+1,j) = norm(test_bc(:,j)-x_vec);

end
end

yLabel = D_bc_te(31,:);
Labels = zeros(1,89);

for i = 1 : 89

if yLabel(:,i) == -1

Labels(1,i) = 2;

end


if yLabel(:,i) == 1

Labels(1,i) = 1;

end
end

yLabel = Labels;

[k,idx] = min(nrm);

a = yLabel - (idx);

nonzero = nnz(a);
error_percentage = (nonzero*100)/length(yLabel);
accuracy = 100 - error_percentage;


fprintf('\t\tPCA Results for  Breast Cancer Test Dataset \n\ntotal instances : 89\n')
fprintf('mis-classifications : %d\n', nonzero)
fprintf('error : %2.4f%% \n', error_percentage)
fprintf('accuracy: %2.4f%% \n\n', accuracy)
