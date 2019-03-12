import Tkinter
import tkFileDialog
mesFormats = [ ('Texte','*.py'),
               ('Windows Bitmap','*.bmp'),
               ('Portable Network Graphics','*.png'),
               ('JPEG / JFIF','*.jpg'),
               ('CompuServer GIF','*.gif'),
               ]
root = Tkinter.Tk()
nomFichier = tkFileDialog.asksaveasfilename(parent=root,filetypes=mesFormats,title="Sauvez l'image sous...")
if len(nomFichier) > 0:
    print "Sauvegarde en cours dans %s" % nomFichier
