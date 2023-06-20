
function varargout = IMAGE(varargin)
% IMAGE MATLAB code for IMAGE.fig
%      IMAGE, by itself, creates a new IMAGE or raises the existing
%      singleton*.
%
%      H = IMAGE returns the handle to a new IMAGE or the handle to
%      the existing singleton*.
%
%      IMAGE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in IMAGE.M with the given input arguments.
%
%      IMAGE('Property','Value',...) creates a new IMAGE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before IMAGE_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to IMAGE_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help IMAGE

% Last Modified by GUIDE v2.5 27-Nov-2022 11:53:22

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @IMAGE_OpeningFcn, ...
                   'gui_OutputFcn',  @IMAGE_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before IMAGE is made visible.
function IMAGE_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to IMAGE (see VARARGIN)

% Choose default command line output for IMAGE
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes IMAGE wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = IMAGE_OutputFcn(hObject, ~, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;

function setGlobal(val)
global file
file=val


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[filename,filepath]=uigetfile({'.';'.jpg';'.png';'*.bmp'},    'Search Image to be Displayed');
fullname=[filepath filename];
t=imread(fullname);
axes(handles.axes1)
imshow(t);
%system('python test.py')
%set(handles.text6,'String',filename);
%py.test.getinput(filename);
setGlobal(filename)



% --- Executes on button press in suggest.
function suggest_Callback(hObject, eventdata, handles)
% hObject    handle to suggest (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
system('python tt.py')
mod = py.importlib.import_module('tt');
py.importlib.reload(mod);
py.tt.getinput(file);
%inputpy = readtable('Recom.csv');
%set(handles.text6,'string',As.csv);
%fid = fopen('Recom.txt','r');
%set(handles.text6,'string',fid);
%a=fscanf(fid,'%f,');
%for i=1:length(a)
    %disp(a(i));
%end
%fclose(fid);
%py.tests.miin();
%str='hi'
%py.tt.improved_recommendations(py.test.get_movie_id());
%set(handles.text6,'string',a)
%set(handles.text6,'String',str);
img=imread('qualified.png');
axes(handles.axes3)
imshow(img);




im=imread(Copy_of_qualified.jpg);
axis(handles.axes5);
imagesc(im);
