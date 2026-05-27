# UNIX Exercise - Initial Website Setup

Welcome! In this assignment, you will copy Hypertext Markup Language (HTML) code for a super-simple web page, upload that web page to a web server, and verify that the web page is indeed live on the web.

## Where we are

A quick explanation of what is going on here.

### Forked repository

If you are viewing this file, then you have most likely **forked** a copy of a **repository** of code. This means that you have made a copy of this repository of code into your own personal account on GitHub.com.

### Clone repository

You will shortly **clone** this personal repository of yours to your own _local_ computer. You may have done this already. Your original copy of this code on GitHub will still remain there, but you will have an additional copy on your own machine.

### Editing code

You will make changes to your local copy of the code using a code editor. And, when you are done modifying the code, you will **push** - i.e. upload - your changes back to your repository on GitHub.com. Doing so shares the changes you made on your own computer with the course instructor and graders who will look at the code in your repository on GitHub.com. This is how you will submit assignments and possibly exams.

### Git

Whether you do so knowingly or not, you are using software called **git** in order to clone - i.e. download - this code to your local machine. You will also use git to push - i.e. upload - your modified code back to GitHub.com when you are done with the assignment.

Git is open source software for **version control**. It helps programmers keep an archive of all the changes they make to their code, and it helps them share those changes they make with other developers.

In our case, you will be using git to share your modified code with the course instructor and graders. You will likely never directly use git - rather, the code editor software we use will trigger git to upload or download code on your behalf without you even knowing it.

### Code editor

To make changes to this code, you will need a **code editor**, also known as an **integrated development environment** (IDE). An IDE or code editor is software that helps developers edit and debug code visually.

Our code editor of choice is [Visual Studio Code](https://code.visualstudio.com), by Microsoft. This is a good free code editor with useful features to help edit and debug code written in most popular programming languages, including Python.

### Files

You will notice that this code repository already contains several files and directories.

- **index.html** - you will write HTML code into this file as part of completing the given assignment.
- **settings.json** - you must edit this file. It contains a few details about this project that help us understand who you are and where your web page is posted only - i.e. what is the web address at which we can view your live web site. You must supply these details into this file, following the example format.
- **README.md** - this file contains instructions written in a relatively easy-to-read formatting notation called Markdown.
- **.gitignore** - a 'hidden' file that instructs the git software not to include certain files when sharing your code with others. This helps you only share the important files. Do not touch this file!
- **tests/** - a directory containing code that will help you determine whether you have completed the assignment correctly or not... more on this later. Do not touch this directory!

## What to do now

Before you can work on the assignment, you will need to perform a few setup tasks.

### Install Visual Studio Code

Download and install the latest version of Visual Studio Code [here](https://code.visualstudio.com).

### Clone this code to your local computer

We will now download this code from GitHub.com into Visual Studio Code on your own computer.

- Open Visual Studio Code
- click the Source Control icon in the left tool bar and then click the button to "Clone Repository".
- A text field will pop open at the top of Visual Studio Code for the web address of the repository to clone. Paste in the address of your personal repository on GitHub and hit Enter.
- A Finder (Mac) / File Explorer (Windows) window will pop open asking you where you would like to save the files in this project. Select a folder/directory where you would like to copy this code, such as your Documents directory.
- Visual Studio Code may ask you to "sign in" to GitHub... do so, if requested.
- Once signed in, Visual Studio Code will download a copy (i.e. a clone) of all the files in your GitHub code repository to a sub-directory of the directory on your own computer that you selected.
- Now open this directory up in Visual Studio Code to see the files.

#### In case you see an error

It seems that Visual Studio Code sometimes pops open a message saying, "Make sure you configure your ‘user.name’ …". To solve this, select the `View`-> `Terminal` menu option.  In the Terminal at the bottom of the window, type in the following commands:

```bash
git config --global user.email "you@example.com" 
git config --global user.name "Your Name". 
```

Replace `you@example.comand` and `Your Name` with the email you used to register for GitHub and your own name, respectively.

## Modify the code

You have now completed the setup and are ready to modify the code, as you will in every assignment.

### Add a few lines of code

You will now add a few line of HTML code to the `index.html` file.

- In Visual Studio Code's Explorer view, open the file named `index.html`.
- In this file, write the lines of HTML code below... try writing them yourself, not copy-and-pasting.
- Where the code below says `Insert your name here exactly as written in your settings.json file`, do exactly that. Your name must be identical in both files.
- Save the file.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>
      Insert your name here exactly as written in your settings.json file
    </title>
  </head>
  <body>
    <h1>Insert your name here exactly as written in your settings.json file</h1>
    <p>Hello world!</p>
  </body>
</html>
```

### Upload the web page to a web server

Upload just the `index.html` file to a web server. Your instructor will have given you instructions for how to do this.

Take note of the web address (URL) of your web page - this is the address that can be plugged into the address bar of any web browser for the web browser to load and display your web page.

### Add your web page's URL to the settings.json file

Make sure this exact URL is placed into the `settings.json` file in the appropriate place. Make sure the URL works when plugged into a web browser beforehand.

### Submit your work on GitHub

You are now ready to submit this assignment. You can do so directly from Visual Studio Code with the following steps, in the indicated order:

1. Switch to the Source Control view in Visual Studio Code - this view will show you a list of the files you have modified.
1. In the "Message" text field towards the top-left, enter a unique message to yourself about what you have changed and, while still with the text field selected, type Command-Enter on Mac OS X, or Control-Enter on Windows, to "commit" the changes you've made with this custom message. If you forget to hit Command-Enter after typing the message, you can instead click the "..." button above the message field and click the "Commit all" option in the menu that appears.
1. Now, click the "..." button above the message field and click the "Push" option in the menu that appears - this will upload your changes to your personal code repository on GitHub.

You have now submitted your completed assignment. Your changes are now posted to GitHub.com, where the instructor and graders can access it. Your `settings.json` file has information about who you are and where we can view your page on the web.

You can verify all this yourself manually by visiting your repository on GitHub.com and making sure the code displayed there is what you submitted.
