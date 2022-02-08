% [fName, dirName] = uigetfile('*.bmp;*.tif;*.jpg;*.tiff;*.png');
% jpg = fullfile(dirName, fName);
% zdj = imread(jpg);
% I = imresize(zdj, [224 224]);
% if(size(I, 3) == 1)
%     I = cat(3, I, I, I);
%     I = double(I);
% end

I = imread("8.jpg");
plik = load('aaa.mat');
plik = plik.net;
YPred = classify(plik, I);
YPred = double(YPred);

%x = (predict(plik, I)).*100;

if(YPred == 1)
%    x1 = x(1);
   text = sprintf('Prawdopodobnie twoja zmiana skórna jest łagodna. W celu zweryfikowania wyniku skontaktuj się z lekarzem.');
end
if(YPred == 2)
%    x2 = x(2);
   text = sprintf('Prawdopodobnie twoja zmiana skórna jest złośliwa. W celu zweryfikowania wyniku skontaktuj się z lekarzem.');
end

save('mat2.mat', 'text')
clear
load('mat2.mat')
% clear
% x = 2+2;
% save("mat1.mat")

