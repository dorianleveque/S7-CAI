#include <QApplication>
#include <QGraphicsScene>
#include <QGraphicsLineItem>
#include <QGraphicsRectItem>
#include <QGraphicsView>
#include <QDebug>
#include <QXmlStreamWriter>
#include <QXmlStreamReader>
#include <QDir>

int main(int argc, char **argv)
{
   QApplication app(argc, argv);
   
   QGraphicsScene scene;
 
   QPen* pen = new QPen();
   pen->setStyle(Qt::DashDotLine);
 
   QBrush* brush = new QBrush();
   brush->setStyle(Qt::CrossPattern);
   

    QGraphicsLineItem *line =scene.addLine(10,20,100,100);
   line->setPen(*pen);
   QGraphicsRectItem *rect = scene.addRect(QRectF(0, 0, 100, 100));
   rect->setBrush(*brush);
   QGraphicsEllipseItem *ellipse =scene.addEllipse(0,0,100,100);


   QGraphicsView view(&scene);

   qDebug() << "line : " << line->type();
   qDebug() << "line pen: " << line->pen();

   qDebug() << "rect : " << rect->type();

   qDebug() << "ellipse : " << ellipse->type();

   view.show();
   
   qDebug() <<  "scene.items().size()" << scene.items().size();
   for (int i =0; i< scene.items().size();i++) { 
     qDebug() <<  "scene.items() :" << scene.items().value(i)->type();
   }    
    QString fileName(QDir::currentPath().append("//scene.xml"));
    QFile file(fileName);
    if (!file.open(QIODevice::WriteOnly))
    {
            return -1;
    }
    QXmlStreamWriter xmlWriter(&file);
    xmlWriter.setAutoFormatting(true);

    xmlWriter.writeStartDocument();
    xmlWriter.writeStartElement("Scene");
    xmlWriter.writeAttribute("version", "v1.0");
    xmlWriter.writeStartElement("GraphicsItemList");
    qreal width, height, x, y;
    for (int i =0; i< scene.items().size();i++) { 
            xmlWriter.writeStartElement("GraphicsItem");
 	    int number=scene.items().value(i)->type();
            xmlWriter.writeAttribute("type", QString::number(number));
	    switch(number) {
	      case 6 :
	      {
		qDebug() << "Line";
		QGraphicsLineItem *line;
		line = qgraphicsitem_cast<QGraphicsLineItem*>(scene.items().value(i));
                x = line->line().x1();
		y = line->line().y1();
		width = line->line().x2();
		height = line->line().y2();
		xmlWriter.writeAttribute("xd", QString::number(x));
 		xmlWriter.writeAttribute("yd", QString::number(y));
		xmlWriter.writeAttribute("xf", QString::number(width));
		xmlWriter.writeAttribute("yf", QString::number(height));
		xmlWriter.writeAttribute("style", QString::number(line->pen().style()));
	      }
		break;
	    }
            xmlWriter.writeEndElement(); // GraphicsItem
    }
   xmlWriter.writeEndElement(); // GraphicsItemList
   xmlWriter.writeEndElement(); // Scene
   file.close();
   
    QString fileReadName(QDir::currentPath().append("//scene.xml"));
    QFile fileRead(fileReadName);
    if (!fileRead.open(QIODevice::ReadOnly))
    {
            return -1;
    }
   
   QXmlStreamReader xmlReader;
   QFile fileread("scene-read.xml");
   qDebug() << "read";
   if (!fileread.open(QFile::ReadOnly | QFile::Text)) { 
     qDebug() << "Error: Cannot read file ";
   }
   xmlReader.setDevice(&fileread);
   while (!xmlReader.atEnd()) {
     if(xmlReader.isStartElement()) {
       if ( xmlReader.name()== "GraphicsItem") {  
	   qDebug() << "graphics";
	   qDebug() << xmlReader.attributes().value("type").toString().toInt();
	   if (xmlReader.attributes().value("type").toString().toInt() == 6 ) {
	     int x=xmlReader.attributes().value("x").toString().toInt();
	     int y=xmlReader.attributes().value("y").toString().toInt();
	     int w=xmlReader.attributes().value("w").toString().toInt();
 	     int h=xmlReader.attributes().value("h").toString().toInt();
	     int style=xmlReader.attributes().value("style").toString().toInt();
	     qDebug() << "read" << x << y<< w << h << style;
 
	     QGraphicsLineItem *ligne = scene.addLine(x,y,w,h);
	     if (style == 0) {
	       ligne->pen().setStyle(Qt::DashDotDotLine);
	     }
	   }
       }
     }
      xmlReader.readNext();
  }
   qDebug() << "end read";
   return app.exec();
}
