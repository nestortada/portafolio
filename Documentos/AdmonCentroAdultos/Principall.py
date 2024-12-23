import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox,QTableWidgetItem
from tabulate import tabulate

from Conex.Conexion import Conexion
from Diseno.DPrincipal import Ui_MainWindow
from Diseno.DAdultos import Ui_AdmonAdultos
from Diseno.DActividades import Ui_AdmonActividades
from Diseno.Dcategoria import Ui_AdmonCategorias
from Diseno.DCentros import Ui_AdmonCentros
from Diseno.DInscripciones import Ui_AdmonInscripciones
from Diseno.DAgregarAdulto import Ui_AgregarAdulto
from Diseno.DModificarAdulto import Ui_ModificarAdulto
from Diseno.DAgregarActividad import Ui_AgregarActividad
from Diseno.DModificarActividad import Ui_ModificarActividad
from Diseno.DAgregarCategoria import Ui_AgregarCategorias
from Diseno.DModificarCategoria import Ui_ModificarCategorias
from Diseno.DAgregarInscripcion import Ui_AgregarInscripciones
from Diseno.DModificarInscripcion import Ui_ModificarInscripcion
from Diseno.DAgregarCentro import Ui_AgregarCentros
from Diseno.DModificarCenrto import Ui_ModificarCentros
from Diseno.DConsultas import Ui_AdmonConsultas

class Principal (QMainWindow):
	def __init__(self):
		super(Principal,self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.BAc.clicked.connect(self.actividad)
		self.ui.BAd.clicked.connect(self.adultos)
		self.ui.BCa.clicked.connect(self.categoria)
		self.ui.BCe.clicked.connect(self.centro)
		self.ui.BCon.clicked.connect(self.consulta)
		self.ui.BIns.clicked.connect(self.inscripcion)
        
		self.ui.BTerminar.clicked.connect(self.cerrar)
		self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
		self.con = Conexion()
		self.miConexion = self.con.conectar()
        
	def cerrar(self):
		self.con.desconectar()
		self.close()
        
	def actividad(self):
		self.ventanaAct = AdmonActividades()
		self.ventanaAct.show()
    
	def adultos(self):
		self.ventanaAd = AdmonAdultos()
		self.ventanaAd.show()
 
	def categoria(self):
		self.ventanaCat = AdmonCategorias()
		self.ventanaCat.show()
 
	def centro(self):
		self.ventanaCen = AdmonCentros()
		self.ventanaCen.show()
 
	def consulta(self):
		self.ventanaCons = AdmonConsultas()
		self.ventanaCons.show()
 
	def inscripcion(self):
		self.ventanaIns = AdmonInscripciones()
		self.ventanaIns.show()
    

        
class AdmonAdultos(QMainWindow):
    def __init__(self):
        super(AdmonAdultos, self).__init__()
        self.ui = Ui_AdmonAdultos()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBTodas.clicked.connect(self.verTodas)
        self.ui.PBBuscar.clicked.connect(self.buscarAdulto)
        self.ui.PBAgregar.clicked.connect(self.agregar)
        self.ui.PBModificar.clicked.connect(self.ModifyAdulto)
        self.ui.PBEliminar.clicked.connect(self.eliminaAdulto)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.ui.PBSalir.clicked.connect(self.cerrar)

    def cerrar(self):
        self.con.desconectar()
        self.close()
        
    def agregar(self):
        self.ventanaAgg = AgregarAdulto()
        self.ventanaAgg.show()
        self.cerrar()
        
    def ModifyAdulto (self):
        self.ventanaMod = ModificarAdulto()
        self.ventanaMod.show()
        self.cerrar()
        
    def verTodas (self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor ()
            mycursor.callproc ('allAdultos')
            
            a = self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)
                
                
            for result in mycursor.stored_results ():
                for (idAdulto, Nombre, Apellido, Nacimiento, Peso, Altura, Contacto, Centro) in result :
                    self.ui.TWTabla.insertRow(cant)
                    
                    celdaCodigo = QTableWidgetItem(str(idAdulto))
                    celdaNombre = QTableWidgetItem(Nombre)
                    celdaApellido = QTableWidgetItem(Apellido)
                    celdaNacimiento = QTableWidgetItem(str(Nacimiento))
                    celdaPeso = QTableWidgetItem(str(Peso))
                    celdaAltura = QTableWidgetItem(str(Altura))
                    celdaContacto = QTableWidgetItem(Contacto)
                    celdaCentro = QTableWidgetItem(Centro)
                    
                    self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                    self.ui.TWTabla.setItem(cant,1,celdaNombre)
                    self.ui.TWTabla.setItem(cant,2,celdaApellido)
                    self.ui.TWTabla.setItem(cant,3,celdaNacimiento)
                    self.ui.TWTabla.setItem(cant,4,celdaPeso)
                    self.ui.TWTabla.setItem(cant,5,celdaAltura)
                    self.ui.TWTabla.setItem(cant,6,celdaContacto)
                    self.ui.TWTabla.setItem(cant,7,celdaCentro)
                    
                    
                    cant = cant + 1
            if cant == 0 :
                QMessageBox.warning(self, "Alerta en Consulta", "No hay Adultos registradas")
            mycursor.close()
        except Exception as miError :
            QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Adultos")
            print(miError)            
    
    def buscarAdulto(self):
        idAdultoBuscar = self.ui.SBCodigoEliminar.value()
        if self.existeIdAdulto(idAdultoBuscar) == False :
            QMessageBox.information(self, "Busqueda Fallida", "La Adulto no existe, no se puede buscar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getAdulto', [idAdultoBuscar])
    
                cant=0
                a = self.ui.TWTabla.rowCount()
                for rep in range(a):
                    self.ui.TWTabla.removeRow(0)
                    
                    
                for result in mycursor.stored_results ():
                    for (idAdulto, Nombre, Apellido, Nacimiento, Peso, Altura, Contacto, Centro) in result :
                        self.ui.TWTabla.insertRow(cant)
                        
                        celdaCodigo = QTableWidgetItem(str(idAdulto))
                        celdaNombre = QTableWidgetItem(Nombre)
                        celdaApellido = QTableWidgetItem(Apellido)
                        celdaNacimiento = QTableWidgetItem(str(Nacimiento))
                        celdaPeso = QTableWidgetItem(str(Peso))
                        celdaAltura = QTableWidgetItem(str(Altura))
                        celdaContacto = QTableWidgetItem(Contacto)
                        celdaCentro = QTableWidgetItem(Centro)
                        
                        self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                        self.ui.TWTabla.setItem(cant,1,celdaNombre)
                        self.ui.TWTabla.setItem(cant,2,celdaApellido)
                        self.ui.TWTabla.setItem(cant,3,celdaNacimiento)
                        self.ui.TWTabla.setItem(cant,4,celdaPeso)
                        self.ui.TWTabla.setItem(cant,5,celdaAltura)
                        self.ui.TWTabla.setItem(cant,6,celdaContacto)
                        self.ui.TWTabla.setItem(cant,7,celdaCentro)
                        
                        
                        cant = cant + 1
    
    
                mycursor.close()
    
            except Exception as miError :
                QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Adultos")
                print(miError)  
                
    def eliminaAdulto(self):
        idAdultoDel = self.ui.SBCodigoEliminar.value()
        if self.existeIdAdulto ( idAdultoDel ) == False :
            QMessageBox.information(self, "Eliminacion Fallida", "El Adulto no existe, no se puede eliminar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delAdulto' , [idAdultoDel] )
                self.miConexion.commit()
                
                QMessageBox.information(self, "Eliminacion Exitosa", "El Adulto ha sido eliminada")
                self.verTodas()
                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Adultos")
                print(miError)
                

    def existeIdAdulto (self,idAdulto):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM AdultoS WHERE idAdulto = %s"
            mycursor.execute(query, [idAdulto])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError) 

class AgregarAdulto(QMainWindow):
    def __init__(self):
        super(AgregarAdulto, self).__init__()
        self.ui = Ui_AgregarAdulto()
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
            
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.ui.PBAgregar.clicked.connect(self.aAd)
        self.ui.PBSalir.clicked.connect(self.close)
        
        
    def aAd(self):
        bandera=1
        idAdultoNew = self.ui.SBCodigo.value()
        if self.existeIdAdulto(idAdultoNew) == True :
            QMessageBox.critical(self,"Error al añadir Adulto","El Adulto ya existe no se puede repetir")
        else :
            nombreNew = self.ui.Nombre.text()
            if nombreNew == "":
                QMessageBox.critical(self,"Error al añadir Adulto","Complete el espacio de nombre")
            else: 
                apellidoNew = self.ui.Apellido.text()
                if apellidoNew == "":
                    QMessageBox.critical(self,"Error al añadir Adulto","Complete el espacio de apellido")
                else:
                    nacimientoNew = self.ui.DTN.date().toString("yyyy-MM-dd")
                    pesoNew = self.ui.DSBP.value()
                    alturaNew = self.ui.SBA.value()
                    contactoNew = self.ui.LC.text()
                    if contactoNew == "":
                        QMessageBox.critical(self,"Error al añadir Adulto","Complete el espacio de contacto")
                    else:
                        if self.ui.CBCentro.isChecked():
                            centroNew = None
                        else:
                            centroNew = self.ui.LCen.text()
                            if self.existeNombre(centroNew) == False :
                                QMessageBox.critical(self,"Error al añadir Adulto","El Centro no existe")
                                bandera=0
                        if bandera==1:
                                    try : 
                                        mycursor = self.miConexion.cursor ()
                                        mycursor.callproc ("newAdulto",[idAdultoNew,nombreNew,apellidoNew,nacimientoNew,pesoNew,alturaNew,contactoNew,centroNew])
                                        self.miConexion.commit ()                
                                        QMessageBox.information(self,"Adulto añadida exitosamente",'La Adulto ha sido creada..!!')
                                        mycursor.close ()
                                    except Exception as miError :
                                        QMessageBox.critical(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de los Adultos")
                                        print(miError)

    def existeIdAdulto (self,idAdulto):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM AdultoS WHERE idAdulto = %s"
            mycursor.execute(query, [idAdulto])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError) 
            
    def existeNombre (self,Nombre):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM CentroS WHERE Nombre = %s"
            mycursor.execute(query, [Nombre])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
class ModificarAdulto(QMainWindow):
    def __init__(self):
        super(ModificarAdulto, self).__init__()
        self.ui = Ui_ModificarAdulto()
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
            
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.ui.PBAgregar.clicked.connect(self.mAd)
        self.ui.PBSalir.clicked.connect(self.close)
        
        
    def mAd(self):
        bandera = 1
        idAdultoViejo = self.ui.SBCodigoViejo.value()
        if self.existeIdAdulto(idAdultoViejo)== False :
            QMessageBox.warning(self, "Error", "El codigo no existe ")
        else:
            idAdultoNew = self.ui.SBCodigo.value()
            if idAdultoNew != idAdultoViejo and self.existeIdAdulto(idAdultoNew) == True:
                QMessageBox.warning(self, "Error","Ya existe una fuente con ese ID, No se puede modificar")
            else:
                nombreNew=self.ui.Nombre.text()
                if nombreNew == "" :
                    QMessageBox.information(self, "Error", " lo dejaste en blanco el nombre")
                else:
                    apellidoNew=self.ui.Apellido.text()
                    if apellidoNew == "" :
                        QMessageBox.information(self, "Error", " lo dejaste en blanco el apellido" )
                    else:
                        nacimientoNew = self.ui.DTN.date().toString("yyyy-MM-dd")
                        pesoNew = self.ui.DSBP.value()
                        alturaNew = self.ui.SBA.value()
                        contactoNew = self.ui.LC.text()
                        if contactoNew == "":
                            QMessageBox.information(self, "Error", " lo dejaste en blanco el apellido" )
                        else:
                            if self.ui.CBCentro.isChecked():
                                centroNew = None
                            else:
                                centroNew = self.ui.LCen.text()
                                if self.existeNombre(centroNew) == False :
                                    QMessageBox.critical(self,"Error","El Centro no existe")
                                    bandera = 0
                                if bandera == 1:
                                    try : 
                                        mycursor = self.miConexion.cursor ()
                                        mycursor.callproc ("modAdulto",[idAdultoNew,nombreNew,apellidoNew,nacimientoNew,pesoNew,alturaNew,contactoNew,centroNew,idAdultoViejo])
                                        self.miConexion.commit ()                
                                        QMessageBox.information(self,"Adulto modificado exitosamente",'El Adulto ha sido creada..!!')
                                        mycursor.close ()
                                    except Exception as miError :
                                        QMessageBox.critical(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de los Adultos")
                                        print(miError)
    def existeNombre (self,Nombre):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM CentroS WHERE Nombre = %s"
            mycursor.execute(query, [Nombre])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)                                
                                
    def existeIdAdulto (self,idAdulto):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM AdultoS WHERE idAdulto = %s"
            mycursor.execute(query, [idAdulto])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError) 
    
        
            
            
class AdmonActividades(QMainWindow):
    def __init__(self):
        super(AdmonActividades, self).__init__()
        self.ui = Ui_AdmonActividades()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBTodas.clicked.connect(self.verTodas)
        self.ui.PBBuscar.clicked.connect(self.buscarActividad)
        self.ui.PBEliminar.clicked.connect(self.eliminaActividad)
        self.ui.PBAgregar.clicked.connect(self.agregarActividad)
        self.ui.PBModificar.clicked.connect(self.modificarActividad)
        
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.ui.PBSalir.clicked.connect(self.cerrar)
    
    def cerrar(self):
        self.con.desconectar()
        self.close()
        
    def verTodas (self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor ()
            mycursor.callproc ('allActividades')
            
            a = self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)
                
                
            for result in mycursor.stored_results ():
                for (idActividad, Nombre, Descripcion, Fecha, iDCategoria, Centro) in result :
                    self.ui.TWTabla.insertRow(cant)
                    
                    celdaCodigo = QTableWidgetItem(str(idActividad))
                    celdaNombre = QTableWidgetItem(Nombre)
                    celdaDescripcion = QTableWidgetItem(Descripcion)
                    celdaFecha = QTableWidgetItem(str(Fecha))
                    celdaCateg = QTableWidgetItem(str(iDCategoria))
                    celdaCentro = QTableWidgetItem(str(Centro))
                    
                    self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                    self.ui.TWTabla.setItem(cant,1,celdaNombre)
                    self.ui.TWTabla.setItem(cant,2,celdaDescripcion)
                    self.ui.TWTabla.setItem(cant,3,celdaFecha)
                    self.ui.TWTabla.setItem(cant,4,celdaCateg)
                    self.ui.TWTabla.setItem(cant,5,celdaCentro)
                    
                    cant = cant + 1
            if cant == 0 :
                QMessageBox.warning(self, "Alerta en Consulta", "No hay Actividades registradas")
            mycursor.close()
        except Exception as miError :
            QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Actividades")
            print(miError)            
    
    def buscarActividad(self):
        idActividadBuscar = self.ui.SBCodigoEliminar.value()
        if self.existeIdActividad(idActividadBuscar) == False :
            QMessageBox.information(self, "Busqueda Fallida", "La Actividad no existe, no se puede buscar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getActividad', [idActividadBuscar])
    
                cant=0
                a = self.ui.TWTabla.rowCount()
                for rep in range(a):
                    self.ui.TWTabla.removeRow(0)
                    
                    
                for result in mycursor.stored_results ():
                    for (idActividad, Nombre, Descripcion, Fecha, iDCategoria, Centro) in result :
                        self.ui.TWTabla.insertRow(cant)
                        
                        celdaCodigo = QTableWidgetItem(str(idActividad))
                        celdaNombre = QTableWidgetItem(Nombre)
                        celdaDescripcion = QTableWidgetItem(Descripcion)
                        celdaFecha = QTableWidgetItem(str(Fecha))
                        celdaCateg = QTableWidgetItem(str(iDCategoria))
                        celdaCentro = QTableWidgetItem(str(Centro))
                        
                        self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                        self.ui.TWTabla.setItem(cant,1,celdaNombre)
                        self.ui.TWTabla.setItem(cant,2,celdaDescripcion)
                        self.ui.TWTabla.setItem(cant,3,celdaFecha)
                        self.ui.TWTabla.setItem(cant,4,celdaCateg)
                        self.ui.TWTabla.setItem(cant,5,celdaCentro)
                        
                        
                        cant = cant + 1
    
    
                mycursor.close()
    
            except Exception as miError :
                QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Actividades")
                print(miError)  
                
    def eliminaActividad(self):
        idActividadDel = self.ui.SBCodigoEliminar.value()
        if self.existeIdActividad ( idActividadDel ) == False :
            QMessageBox.information(self, "Eliminacion Fallida", "La Actividad no existe, no se puede eliminar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delActividad' , [idActividadDel] )
                self.miConexion.commit()
                
                QMessageBox.information(self, "Eliminacion Exitosa", "La Actividad ha sido eliminada")
                self.verTodas()
                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Eliminacion de la Actividad")
                print(miError)
                
    def agregarActividad(self):
        self.ventanaAct = AgregarActividad()
        self.ventanaAct.show()
        self.cerrar()
    
    def modificarActividad(self):
        self.ventanaMAct = ModificarActividad()
        self.ventanaMAct.show()
        self.cerrar()

    def existeIdActividad (self,idActividad):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Actividades WHERE idActividad = %s"
            mycursor.execute(query, [idActividad])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
class AgregarActividad (QMainWindow):
    def __init__(self):
        super(AgregarActividad, self).__init__()
        self.ui =Ui_AgregarActividad()
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBAgregar.clicked.connect(self.agregar)
        self.ui.PBSalir.clicked.connect(self.close)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        
    def agregar(self):
        bandera = 1
        idActividadNew =self.ui.SBCodigo.value()
        if self.existeIdActividad(idActividadNew) == True:
            QMessageBox.information(self, "Error", "El codigo ya existe")
        else: 
            nombreNew = self.ui.Nombre.text()
            if nombreNew == "":
                QMessageBox.information(self, "Error", " lo dejaste en blanco el nombre")
            else:
                descripcionNew= self.ui.Descripcion.text()
                if descripcionNew == "":
                    QMessageBox.information(self, "Error", " lo dejaste en blanco la descripcion")
                else:
                    if self.ui.CBFecha.isChecked():
                        fechaNew= None
                    else:
                        fechaNew = self.ui.Fecha.date().toString("yyyy-MM-dd")
                        
                    if self.ui.CBCategoria.isChecked():
                        idCategoriaNew = None
                    else:
                        idCategoriaNew = self.ui.SBCodigoCategoria.value()
                        
                        if self.existeIdCategoria(idActividadNew) == False:
                            QMessageBox.information(self, "Error", "No has creado una categoria con este codigo")
                            bandera = 0
                    if bandera == 1:
                        if self.ui.CBCentro.isChecked():
                            centroNew = None
                        else:
                            centroNew = self.ui.Centro.text()
                            
                            if self.existeNombre(centroNew) == False:
                                QMessageBox.information(self, "Error", "No has creado un nombre en centros")
                                bandera =0
                        if bandera ==1:
                            try : 
                                mycursor = self.miConexion.cursor ()
                                mycursor.callproc ("newActividad",[ idActividadNew,nombreNew,descripcionNew,fechaNew, idCategoriaNew,centroNew])
                                self.miConexion.commit ()                
                                QMessageBox.information(self,"Actividad añadida exitosamente",'La Actividad ha sido creada..!!')
                                mycursor.close ()
                            except Exception as miError :
                                QMessageBox.critical(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las actividades")
                                print(miError)
            
    def existeIdActividad (self,idActividad):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Actividades WHERE idActividad = %s"
            mycursor.execute(query, [idActividad])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
    def existeIdCategoria (self,idCategoria):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Categorias WHERE idCategoria = %s"
            mycursor.execute(query, [idCategoria])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)         
    
    def existeNombre (self,Nombre):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM CentroS WHERE Nombre = %s"
            mycursor.execute(query, [Nombre])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)

class ModificarActividad(QMainWindow):
    def __init__(self):
        super(ModificarActividad, self).__init__()
        self.ui = Ui_ModificarActividad()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBAgregar.clicked.connect(self.modificar)
        self.ui.PBSalir.clicked.connect(self.close)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        
    def modificar(self):
        bandera=1
        idActividadOld = self.ui.SBCodigoViejo.value()
        if self.existeIdActividad(idActividadOld)== False:
            QMessageBox.information(self, "Error", "El codigo no existe para modificarlo ")
        else:
            idActividadNew = self.ui.SBCodigo.value()
            if idActividadNew != idActividadOld and self.existeIdActividad(idActividadNew) == True :
                QMessageBox.information(self, "Error", "El codigo ya existe")
            else:
                nombreNew = self.ui.Nombre.text()
                if nombreNew == "":
                    QMessageBox.information(self, "Error", " lo dejaste en blanco el nombre ")
                else:
                    descripcionNew= self.ui.Descripcion.text()
                    if descripcionNew == "":
                        QMessageBox.information(self, "Error", " lo dejaste en blanco la descripcion")
                    else:
                        if self.ui.CBFecha.isChecked():
                            fechaNew = None
                        else:
                            fechaNew = self.ui.Fecha.date().toString("yyyy-MM-dd")
                            
                        if self.ui.CBCategoria.isCheckable():
                            idCategoriaNew = None
                        else:
                            idCategoriaNew = self.ui.SBCodigoCategoria.value()
                            if self.existeIdCategoria(idCategoriaNew) == False:
                                QMessageBox.information(self, "Error", "No has creado una categoria con este codigo")
                                bandera=0
                        if bandera ==1:
                            if self.ui.CBCentro.isChecked():
                                centroNew = None
                            else:
                                centroNew = self.ui.Centro.text()
                                if self.existeNombre(centroNew) == False:
                                    QMessageBox.information(self, "Error", "No has creado un nombre al centro")
                                    bandera=0
                            if bandera ==1:
                                try : 
                                    mycursor = self.miConexion.cursor ()
                                    mycursor.callproc ("modActividad",[ idActividadNew,nombreNew,descripcionNew,fechaNew, idCategoriaNew,centroNew, idActividadOld])
                                    self.miConexion.commit ()                
                                    QMessageBox.information(self,"Actividad modificada exitosamente",'La Actividad ha sido creada..!!')
                                    mycursor.close ()
                                except Exception as miError :
                                    QMessageBox.critical(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las actividades")
                                    print(miError)
                            
        
    def existeIdActividad (self,idActividad):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Actividades WHERE idActividad = %s"
            mycursor.execute(query, [idActividad])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)    
            
    def existeIdCategoria (self,idCategoria):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Categorias WHERE idCategoria = %s"
            mycursor.execute(query, [idCategoria])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)         
    
    def existeNombre (self,Nombre):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM CentroS WHERE Nombre = %s"
            mycursor.execute(query, [Nombre])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)      
            
class AdmonCategorias(QMainWindow):
    def __init__(self):
        super(AdmonCategorias, self).__init__()
        self.ui = Ui_AdmonCategorias()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBTodas.clicked.connect(self.verTodas)
        self.ui.PBBuscar.clicked.connect(self.buscarCategoria)
        self.ui.PBEliminar.clicked.connect(self.eliminaCategoria)
        self.ui.PBAgregar.clicked.connect(self.agregarCategoria)
        self.ui.PBModificar.clicked.connect(self.modificarCategoria)
        
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.ui.PBSalir.clicked.connect(self.cerrar)
    
    def cerrar(self):
        self.con.desconectar()
        self.close()
        
    def verTodas (self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor ()
            mycursor.callproc ('allCategorias')
            
            a = self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)
                
                
            for result in mycursor.stored_results ():
                for (idCategoria, Nombre) in result :
                    self.ui.TWTabla.insertRow(cant)
                    
                    celdaCodigo = QTableWidgetItem(str(idCategoria))
                    celdaNombre = QTableWidgetItem(Nombre)
                    
                    self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                    self.ui.TWTabla.setItem(cant,1,celdaNombre)
                    
                    cant = cant + 1
            if cant == 0 :
                QMessageBox.warning(self, "Alerta en Consulta", "No hay Categoriaes registradas")
            mycursor.close()
        except Exception as miError :
            QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Categoriaes")
            print(miError)            
    
    def buscarCategoria(self):
        idCategoriaBuscar = self.ui.SBCodigoEliminar.value()
        if self.existeIdCategoria(idCategoriaBuscar) == False :
            QMessageBox.information(self, "Busqueda Fallida", "La Categoria no existe, no se puede buscar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getCategoria', [idCategoriaBuscar])
    
                cant=0
                a = self.ui.TWTabla.rowCount()
                for rep in range(a):
                    self.ui.TWTabla.removeRow(0)
                    
                    
                for result in mycursor.stored_results ():
                    for (idCategoria, Nombre) in result :
                        self.ui.TWTabla.insertRow(cant)
                        
                        celdaCodigo = QTableWidgetItem(str(idCategoria))
                        celdaNombre = QTableWidgetItem(Nombre)
                        
                        self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                        self.ui.TWTabla.setItem(cant,1,celdaNombre)
                        
                        cant = cant + 1
    
    
                mycursor.close()
    
            except Exception as miError :
                QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Categoriaes")
                print(miError)  
                
    def eliminaCategoria(self):
        idCategoriaDel = self.ui.SBCodigoEliminar.value()
        if self.existeIdCategoria ( idCategoriaDel ) == False :
            QMessageBox.information(self, "Eliminacion Fallida", "La Categoria no existe, no se puede eliminar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delCategoria' , [idCategoriaDel] )
                self.miConexion.commit()
                
                QMessageBox.information(self, "Eliminacion Exitosa", "La Categoria ha sido eliminada")
                self.verTodas()
                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Eliminacion de la Categoria")
                print(miError)
    
    def agregarCategoria(self):
        self.ventanaACat = AgregarCategoria()
        self.ventanaACat.show()
        self.cerrar()
        
    def modificarCategoria(self):
        self.ventanaMCat = ModificarCategoria()
        self.ventanaMCat.show()
        self.cerrar()
    
    def existeIdCategoria (self,idCategoria):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Categorias WHERE idCategoria = %s"
            mycursor.execute(query, [idCategoria])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
class AgregarCategoria(QMainWindow):
    def __init__(self):
        super(AgregarCategoria, self).__init__()
        self.ui = Ui_AgregarCategorias()
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBAgregar.clicked.connect(self.agregar)
        self.ui.PBSalir.clicked.connect(self.close)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        
    def agregar(self):
        idCategoriaNew = self.ui.SBCodigo.value()
        if self.existeIdCategoria(idCategoriaNew) == True:
            QMessageBox.information(self, "Error", "El codigo ya existe")
        else:
            nombreNew = self.ui.Nombre.text()
            if nombreNew == "":
                QMessageBox.information(self, "Error", " lo dejaste en blanco el nombre")
            else:
                try : 
                    mycursor = self.miConexion.cursor ()
                    mycursor.callproc ("newCategoria",[idCategoriaNew, nombreNew])
                    self.miConexion.commit ()                
                    QMessageBox.information(self,"Categoria añadida exitosamente",'La Categoria ha sido creada..!!')
                    mycursor.close ()
                except Exception as miError :
                    QMessageBox.critical(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las categorias")
                    print(miError)
        
        
    def existeIdCategoria (self,idCategoria):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Categorias WHERE idCategoria = %s"
            mycursor.execute(query, [idCategoria])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)    
            
class ModificarCategoria(QMainWindow):
    def __init__(self):
        super(ModificarCategoria, self).__init__()
        self.ui = Ui_ModificarCategorias()
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBAgregar.clicked.connect(self.modificar)
        self.ui.PBSalir.clicked.connect(self.close)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
    
    def modificar(self):
        idCategoriaOld = self.ui.SBCodigoViejo.value()
        if self.existeIdCategoria(idCategoriaOld)== False:
            QMessageBox.information(self, "ERROR", "EL codigo no existe")
        else:
            idCategoriaNew = self.ui.SBCodigo.value()
            if idCategoriaNew != idCategoriaOld and self.existeIdCategoria(idCategoriaNew)== True :
                QMessageBox.information(self, "Error", "El codigo ya existe")
            else:
                nombreNew = self.ui.Nombre.text()
                if nombreNew == "":
                    QMessageBox.information(self, "Error", " lo dejaste en blanco el nombre")
                else:
                    try : 
                        mycursor = self.miConexion.cursor ()
                        mycursor.callproc ("modCategoria",[idCategoriaNew, nombreNew, idCategoriaOld])
                        self.miConexion.commit ()                
                        QMessageBox.information(self,"Categoria modificada exitosamente",'La Categoria ha sido modificada..!!')
                        mycursor.close ()
                    except Exception as miError :
                        QMessageBox.critical(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las categorias")
                        print(miError)
        
    def existeIdCategoria (self,idCategoria):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Categorias WHERE idCategoria = %s"
            mycursor.execute(query, [idCategoria])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)    
            
class AdmonInscripciones(QMainWindow):
    def __init__(self):
        super(AdmonInscripciones, self).__init__()
        self.ui = Ui_AdmonInscripciones()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBTodas.clicked.connect(self.verTodas)
        self.ui.PBBuscar.clicked.connect(self.buscarInscripcion)
        self.ui.PBEliminar.clicked.connect(self.eliminaInscripcion)
        self.ui.PBAgregar.clicked.connect(self.agregarInscripcion)
        self.ui.PBModificar.clicked.connect(self.modificarInscripciones)
        
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.ui.PBSalir.clicked.connect(self.cerrar)
    
    def cerrar(self):
        self.con.desconectar()
        self.close()
        
    def verTodas (self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor ()
            mycursor.callproc ('allInscripciones')
            
            a = self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)
                
                
            for result in mycursor.stored_results ():
                for (idAdulto, idActividad, Calificacion) in result :
                    self.ui.TWTabla.insertRow(cant)
                    
                    celdaCodAd = QTableWidgetItem(str(idAdulto))
                    celdaCodAc = QTableWidgetItem(str(idActividad))
                    celdaCalificacion = QTableWidgetItem(str(Calificacion))
                    
                    self.ui.TWTabla.setItem(cant,0,celdaCodAd)
                    self.ui.TWTabla.setItem(cant,1,celdaCodAc)
                    self.ui.TWTabla.setItem(cant,2,celdaCalificacion)
                    
                    cant = cant + 1
            if cant == 0 :
                QMessageBox.warning(self, "Alerta en Consulta", "No hay Inscripciones registradas")
            mycursor.close()
        except Exception as miError :
            QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Inscripciones")
            print(miError)            
    
    def buscarInscripcion(self):
        idAdultoBuscar = self.ui.SBCodigoEliminarAd.value()
        if self.existeAdultoIns(idAdultoBuscar) == False :
            QMessageBox.information(self, "Busqueda Fallida", "La Inscripcion no existe, no se puede buscar")
        idActividadBuscar = self.ui.SBCodigoEliminarAc.value()
        if self.existeActividadIns(idActividadBuscar) == False :
            QMessageBox.information(self, "Busqueda Fallida", "La Inscripcion no existe, no se puede buscar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getInscripcion', [idAdultoBuscar, idActividadBuscar])
    
                cant=0
                a = self.ui.TWTabla.rowCount()
                for rep in range(a):
                    self.ui.TWTabla.removeRow(0)
                    
                    
                for result in mycursor.stored_results ():
                    for (idAdulto, idActividad, Calificacion) in result :
                        self.ui.TWTabla.insertRow(cant)
                        
                        celdaCodAd = QTableWidgetItem(str(idAdulto))
                        celdaCodAc = QTableWidgetItem(str(idActividad))
                        celdaCalificacion = QTableWidgetItem(str(Calificacion))
                        
                        self.ui.TWTabla.setItem(cant,0,celdaCodAd)
                        self.ui.TWTabla.setItem(cant,1,celdaCodAc)
                        self.ui.TWTabla.setItem(cant,2,celdaCalificacion)
                        
                        cant = cant + 1
    
    
                mycursor.close()
    
            except Exception as miError :
                QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Inscripciones")
                print(miError)  
                
    def eliminaInscripcion(self):
        idAdultoDel = self.ui.SBCodigoEliminarAd.value()
        if self.existeAdultoIns(idAdultoDel) == False :
            QMessageBox.information(self, "Busqueda Fallida", "El Adulto no existe, no se puede buscar")
        idActividadDel = self.ui.SBCodigoEliminarAc.value()
        if self.existeActividadIns(idActividadDel) == False :
            QMessageBox.information(self, "Busqueda Fallida", "La Actividad no existe, no se puede buscar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delInscripcion' , [idAdultoDel, idActividadDel] )
                self.miConexion.commit()
                
                QMessageBox.information(self, "Eliminacion Exitosa", "El Inscripcione ha sido eliminada")
                self.verTodas()
                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Eliminacion de Inscripcion")
                print(miError)
                
    def agregarInscripcion(self):
        self.ventanaAIns = AgregarInscripcion()
        self.ventanaAIns.show()
        self.cerrar()
    
    def modificarInscripciones(self):
        self.ventanaMIns = ModificarInscripcion()
        self.ventanaMIns.show()
        self.cerrar()

    def existeAdultoIns (self,idAdulto):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Inscripciones WHERE idAdulto = %s"
            mycursor.execute(query, [idAdulto])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError) 
            
    def existeActividadIns (self,Actividad):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Inscripciones WHERE idActividad = %s"
            mycursor.execute(query, [Actividad])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError) 

class AgregarInscripcion(QMainWindow):
    def __init__(self):
        super(AgregarInscripcion, self).__init__()
        self.ui = Ui_AgregarInscripciones()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBAgregar.clicked.connect(self.agregar)
        self.ui.PBSalir.clicked.connect(self.close)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        
    def agregar(self):
        
        idAdultoNew = self.ui.CodigoAdulto.value()
        if self.existeIdAdulto(idAdultoNew)==False:
            QMessageBox.information(self, "EROR", "EL codigo no existe")
        else:
            idActividadNew = self.ui.CodigoACtividad.value()
            if self.existeIdActividad(idActividadNew) == False:
                QMessageBox.information(self, "EROR", "EL codigo no existe")
            else:
                if self.existeInscripcion(idAdultoNew, idActividadNew) == True:
                    QMessageBox.information(self, "ERROR", "La inscripción ya existe")
                else:
                    if self.ui.CBCali.isChecked():
                        calificacionNew = None
                    else:
                        calificacionNew = self.ui.Calificacion.value()
                    try : 
                        mycursor = self.miConexion.cursor ()
                        mycursor.callproc ("newInscripcion",[idAdultoNew,idActividadNew,calificacionNew])
                        self.miConexion.commit ()                
                        QMessageBox.information(self,"Inscripcion Añadida exitosamente",'La Inscripcion ha sido creado..!!')
                        mycursor.close ()
                    except Exception as miError :
                        QMessageBox.critical(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las inscriipciones")
                        print(miError)    
                    
    def existeIdAdulto (self,idAdulto):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM AdultoS WHERE idAdulto = %s"
            mycursor.execute(query, [idAdulto])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError) 
            
    def existeIdActividad (self,idActividad):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Actividades WHERE idActividad = %s"
            mycursor.execute(query, [idActividad])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)    
            
    def existeInscripcion(self, idAdulto, idActividad):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM Inscripciones WHERE idAdulto = %s AND idActividad = %s"
            mycursor.execute(query, (idAdulto, idActividad))
            resultados = mycursor.fetchone()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)        

class ModificarInscripcion(QMainWindow):
    def __init__(self):
        super(ModificarInscripcion, self).__init__()
        self.ui = Ui_ModificarInscripcion()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBAgregar.clicked.connect(self.modificar)
        self.ui.PBSalir.clicked.connect(self.close)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        
    def modificar(self):
        idAdultoOld = self.ui.CodigoAdultoViejo.value()
        idActividadOld = self.ui.CodigoACtividadVieja.value()
        if self.existeInscripcion(idAdultoOld , idActividadOld) == False:
            QMessageBox.information(self, "ERROR", "La inscripción no existe en esos codigos para ser remplazados ")
        else:
            idAdultoNew = self.ui.CodigoAdulto.value()
            if self.existeIdAdulto(idAdultoNew)==False:
                QMessageBox.information(self, "EROR", "EL codigo no existe")
            else:
                idActividadNew = self.ui.CodigoACtividad.value()
                if self.existeIdActividad(idActividadNew) == False:
                    QMessageBox.information(self, "EROR", "EL codigo no existe")
                else:
                    if self.existeInscripcion(idAdultoNew, idActividadNew) == True and (idActividadNew != idActividadOld and idAdultoOld != idAdultoNew):
                        QMessageBox.information(self, "ERROR", "La inscripción ya existe")
                    else:
                        if self.ui.CBCali.isChecked():
                            calificacionNew = None
                        else:
                            calificacionNew = self.ui.Calificacion.value()
                        try:
                            mycursor = self.miConexion.cursor ()
                            mycursor.callproc ("modInscripcion",[idAdultoNew,idActividadNew,calificacionNew,idAdultoOld,idActividadOld])
                            self.miConexion.commit ()                
                            QMessageBox.information(self,"Inscripcion modificada exitosamente",'La Inscripcion ha sido modificada..!!')
                            mycursor.close ()
                        except Exception as miError :
                            QMessageBox.critical(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las inscriipciones")
                            print(miError) 
                    
    def existeIdAdulto (self,idAdulto):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM AdultoS WHERE idAdulto = %s"
            mycursor.execute(query, [idAdulto])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError) 
            
    def existeIdActividad (self,idActividad):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Actividades WHERE idActividad = %s"
            mycursor.execute(query, [idActividad])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)    
            
    def existeInscripcion(self, idAdulto, idActividad):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT count(*) FROM Inscripciones WHERE idAdulto = %s AND idActividad = %s"
            mycursor.execute(query, (idAdulto, idActividad))
            resultados = mycursor.fetchone()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)    
         
class AdmonCentros(QMainWindow):
    def __init__(self):
        super(AdmonCentros, self).__init__()
        self.ui = Ui_AdmonCentros()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.PBTodas.clicked.connect(self.verTodas)
        self.ui.PBBuscar.clicked.connect(self.buscarCentro)
        self.ui.PBAgregar.clicked.connect(self.agregar)
        self.ui.PBModificar.clicked.connect(self.modificar)
        self.ui.PBEliminar.clicked.connect(self.eliminaCentro)
        
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.ui.PBSalir.clicked.connect(self.cerrar)
    
    def cerrar(self):
        self.con.desconectar()
        self.close()

    def agregar(self):
        self.ventanaAgg = AgregarCentro()
        self.ventanaAgg.show()
        self.cerrar()

    def modificar(self):
        self.ventanaMod = ModifyCentro()
        self.ventanaMod.show()
        self.cerrar()
        
    def verTodas (self):
        cant = 0
        try:
            mycursor = self.miConexion.cursor()
            mycursor.execute("CALL allCentros()")  # Ejecuta el procedimiento directamente
            
            results = mycursor.fetchall()
            a = self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)
            
            for (Nombre, Direccion, Telefono) in results:
                self.ui.TWTabla.insertRow(cant)
                
                celdaNombre = QTableWidgetItem(Nombre)
                celdaDireccion = QTableWidgetItem(Direccion)
                celdaTelefono = QTableWidgetItem(Telefono)
                
                self.ui.TWTabla.setItem(cant, 0, celdaNombre)
                self.ui.TWTabla.setItem(cant, 1, celdaDireccion)
                self.ui.TWTabla.setItem(cant, 2, celdaTelefono)
                
                cant += 1
            if cant == 0:
                QMessageBox.warning(self, "Alerta en Consulta", "No hay Centros registradas")
            mycursor.close()
        except Exception as miError:
            QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de las Centros")
            print(miError)

    def buscarCentro(self):
        NombreBuscar = self.ui.SBCodigoEliminar.text()
        if not self.existeNombre(NombreBuscar):
            QMessageBox.critical(self, "Búsqueda Fallida", "El Centro no existe, no se puede buscar")
            return
        
        try:
            mycursor = self.miConexion.cursor()
            mycursor.callproc('getCentro', [NombreBuscar])
            
            # Limpiar la tabla
            cant = 0
            a = self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)

            # Procesar resultados
            results_found = False
            for result in mycursor.fetchall():
                results_found = True
                Nombre, Direccion, Telefono = result
                self.ui.TWTabla.insertRow(cant)
                
                celdaNombre = QTableWidgetItem(Nombre)
                celdaDireccion = QTableWidgetItem(Direccion)
                celdaTelefono = QTableWidgetItem(Telefono)
                
                self.ui.TWTabla.setItem(cant, 0, celdaNombre)
                self.ui.TWTabla.setItem(cant, 1, celdaDireccion)
                self.ui.TWTabla.setItem(cant, 2, celdaTelefono)
                
                cant += 1
            
            if not results_found:
                QMessageBox.warning(self, "Búsqueda Fallida", "No se encontraron resultados para el Centro buscado")
            
            mycursor.close()
        
        except Exception as miError:
            QMessageBox.warning(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de los Centros")
            print("Error:", miError)  # Depuración

  
                
    def eliminaCentro(self):
        NombreDel = self.ui.SBCodigoEliminar.text()
        if self.existeNombre ( NombreDel ) == False :
            QMessageBox.information(self, "Eliminacion Fallida", "El Centro no existe, no se puede eliminar")
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delCentro' , [NombreDel] )
                self.miConexion.commit()
                
                QMessageBox.information(self, "Eliminacion Exitosa", "El Centro ha sido eliminado")
                self.verTodas()
                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Eliminacion de El Centro")
                print(miError)

    def existeNombre (self,Nombre):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Centros WHERE Nombre = %s"
            mycursor.execute(query, [Nombre])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError) 
            
class AgregarCentro(QMainWindow):
    def __init__(self):
        super(AgregarCentro, self).__init__()
        self.ui = Ui_AgregarCentros()
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
            
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.ui.PBAgregar.clicked.connect(self.aCe)
        self.ui.PBSalir.clicked.connect(self.close)
        
    def aCe(self):
        nombreNew = self.ui.Nombre.text()
        if self.existeNombre(nombreNew) == True :
            QMessageBox.critical(self,"Error al añadir Centro","El Centro ya existe no se puede repetir")
        elif nombreNew == "":
            QMessageBox.critical(self,"Error al añadir Centro","Ingrese el nombre")
        else :
            direccionNew = self.ui.Direccion.text()
            telefonoNew = self.ui.Telefono.text()
            if direccionNew == "":
                QMessageBox.critical(self,"Error al añadir Centro","Ingrese la direccion")
            else:
                if (self.existeDireccion(direccionNew)== True):
                    QMessageBox.information(self, "Error", "La direccion ya ha sido creada")
                else: 
                   if telefonoNew == "":
                       QMessageBox.critical(self,"Error al añadir Centro","Ingrese el telefono")
                   else:
                       if (self.existeTelefono(telefonoNew)== True):
                           QMessageBox.information(self, "Error", "El telefono ya ha sido creada")
                       else: 
                            try : 
                                mycursor = self.miConexion.cursor ()
                                mycursor.callproc ("newCentro",[nombreNew,direccionNew,telefonoNew])
                                self.miConexion.commit ()                
                                QMessageBox.information(self,"Centro añadido exitosamente",'El Centro ha sido creado..!!')
                                mycursor.close ()
                            except Exception as miError :
                                QMessageBox.critical(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de los Centros")
                                print(miError)

    def existeNombre (self,Nombre):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Centros WHERE Nombre = %s"
            mycursor.execute(query, [Nombre])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
    def existeDireccion(self,direccion):
         try :
             mycursor = self.miConexion.cursor ()
             query = "SELECT count(*) FROM Centros WHERE Direccion = %s"
             mycursor.execute(query, [direccion])      
             resultados=mycursor.fetchall()
             for registro in resultados:
                 if  registro[0] == 1 :
                     return True
                 return False
         except Exception as miError:
             print('Fallo ejecutando el procedimiento')
             print(miError)
             
    def existeTelefono(self,telefono):
         try :
             mycursor = self.miConexion.cursor ()
             query = "SELECT count(*) FROM Centros WHERE Telefono = %s"
             mycursor.execute(query, [telefono])      
             resultados=mycursor.fetchall()
             for registro in resultados:
                 if  registro[0] == 1 :
                     return True
                 return False
         except Exception as miError:
             print('Fallo ejecutando el procedimiento')
             print(miError)      
             
class ModifyCentro(QMainWindow):
    def __init__(self):
        super(ModifyCentro, self).__init__()
        self.ui = Ui_ModificarCentros()
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
            
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.ui.PBAgregar.clicked.connect(self.aCe)
        self.ui.PBSalir.clicked.connect(self.close)

    def aCe(self):
        nombreOld = self.ui.NombreViejo.text()
        if self.existeNombre(nombreOld) == False:
            QMessageBox.critical(self, "Error al añadir Centro", "El Centro que desea modificar no existe")
        elif nombreOld == "":
            QMessageBox.critical(self, "Error al añadir Centro", "Ingrese el nombre que desea modificar")
        else:
            nombreNew = self.ui.Nombre.text()
            if nombreOld.lower() != nombreNew.lower() and self.existeNombre(nombreNew) == True:
                QMessageBox.critical(self, "Error al añadir Centro", "El Centro ya existe no se puede repetir")
            elif nombreNew == "":
                QMessageBox.critical(self, "Error al añadir Centro", "Ingrese el nombre")
            else:
                direccionNew = self.ui.Direccion.text()
                if direccionNew == "":
                    QMessageBox.critical(self, "Error al añadir Centro", "Ingrese la direccion")
                else:
                    BuscarDireccion = self.BuscarDireccion(nombreOld)
                    if BuscarDireccion is not None and direccionNew.lower() != BuscarDireccion.lower() and self.existeDireccion(direccionNew) == True:
                        QMessageBox.information(self, "Error", "La direccion ya ha sido creada")
                    else:
                        telefonoNew = self.ui.Telefono.text()
                        if telefonoNew == "":
                            QMessageBox.critical(self, "Error al añadir Centro", "Ingrese el telefono")
                        else:
                            BuscarTelefono = self.BuscarTelefono(nombreOld)
                            if BuscarTelefono is not None and telefonoNew.lower() != BuscarTelefono.lower() and self.existeTelefono(telefonoNew) == True:
                                QMessageBox.information(self, "Error", "El telefono ya ha sido creada")
                            else:
                                try:
                                    mycursor = self.miConexion.cursor()
                                    mycursor.callproc("modCentro", [nombreNew, direccionNew, telefonoNew, nombreOld])
                                    self.miConexion.commit()
                                    QMessageBox.information(self, "Centro añadido exitosamente", 'El Centro ha sido modificado..!!')
                                    mycursor.close()
                                except Exception as miError:
                                    QMessageBox.critical(self, "Consulta Fallida", "Fallo ejecutando el procedimiento de Consulta de los Centros")
                                    print(miError)


    def existeNombre (self,Nombre):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Centros WHERE Nombre = %s"
            mycursor.execute(query, [Nombre])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
    def BuscarDireccion(self,Nombre):
       try:
           mycursor = self.miConexion.cursor()
           mycursor.execute("SELECT Direccion FROM Centros WHERE Nombre = %s", (Nombre,))
           resultado=mycursor.fetchone()
           direccion = resultado[0]
           return direccion
       except Exception as miError:
           print('Fallo ejecutando el procedimiento')
           print(miError)
           
    def BuscarTelefono(self,Nombre):
       try:
           mycursor = self.miConexion.cursor()
           mycursor.execute("SELECT Telefono FROM Centros WHERE Nombre = %s", (Nombre,))
           resultado=mycursor.fetchone()
           telefono = resultado[0]
           return telefono
       except Exception as miError:
           print('Fallo ejecutando el procedimiento')
           print(miError)       
           
    def existeDireccion(self,direccion):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Centros WHERE Direccion = %s"
            mycursor.execute(query, [direccion])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
    def existeTelefono(self,telefono):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM Centros WHERE Telefono = %s"
            mycursor.execute(query, [telefono])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
class AdmonConsultas(QMainWindow):
    def __init__(self):
        super(AdmonConsultas, self).__init__()
        self.ui = Ui_AdmonConsultas()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        self.ui.BLAM.clicked.connect(self.cons1)
        self.ui.BLAF.clicked.connect(self.cons2)
        self.ui.BCAA.clicked.connect(self.cons3)
        self.ui.BLIA.clicked.connect(self.cons4)
        self.ui.BAC.clicked.connect(self.cons5)
        self.ui.BEx.clicked.connect(self.cons6)
        
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint, False)
        self.ui.BTerminar.clicked.connect(self.cerrar)
        
    def cons1(self):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT c.Nombre AS Centro, a.Nombre, a.Apellido FROM Centros c JOIN Adultos a ON c.Nombre = a.Centro ORDER BY c.Nombre ASC, a.Apellido ASC;"
            mycursor.execute(query)
            resultados = mycursor.fetchall()
    
            tabla_resultados = []
            for registro in resultados:
                tabla_resultados.append([registro[0], registro[1], registro[2]])
    
            headers = ["Centro", "Nombre", "Apellido"]
            tabla = tabulate(tabla_resultados, headers, tablefmt="pretty")
    
            QMessageBox.information(self, 'Listado de Adultos Mayores por Centro', tabla)
    
            mycursor.close()
        except Exception as miError:
            print("Fallo ejecutando el procedimiento..!!")
            print(miError)
            
    def cons2(self):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT c.Nombre AS 'Categoria', a.Fecha, a.Nombre AS 'Actividad', a.Descripcion, ce.Direccion FROM Actividades a INNER JOIN Categorias c ON a.iDCategoria = c.idCategoria INNER JOIN Centros ce ON a.Centro = ce.Nombre;"
            mycursor.execute(query)
            resultados = mycursor.fetchall()
    
            tabla_resultados = []
            for registro in resultados:
                tabla_resultados.append([registro[0],"-",registro[1],"-",registro[2],"-",registro[3],"-",registro[4]])
    
            tabla = tabulate(tabla_resultados, tablefmt="plain")
    
            QMessageBox.information(self,"Listado de Actividades Futuras",tabla)
    
            mycursor.close()
        except Exception as miError:
            print("Fallo ejecutando el procedimiento..!!")
            print(miError)
            
    def cons3(self):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT a.Nombre AS 'Actividad', ad.Nombre AS 'Adulto Mayor', i.Calificacion AS 'Calificación de Actividad' FROM Inscripcion i INNER JOIN Adultos ad ON ad.idAdulto = i.IdAdulto INNER JOIN Actividades a ON a.idActividad = i.IdActividad ORDER BY i.Calificacion DESC;"
            mycursor.execute(query)
            resultados = mycursor.fetchall()
            
            tabla_resultados = []
            for registro in resultados:
                tabla_resultados.append([registro[0], registro[1], registro[2]])
            
            headers = ["Actividad", "Adulto Mayor", "Calificación de Actividad"]
            tabla = tabulate(tabla_resultados, headers, tablefmt="pretty")
            
            QMessageBox.information(self,"Calificación de una Actividad",tabla)
            mycursor.close()
        except Exception as miError:
            print("Fallo ejecutando el procedimiento..!!")
            print(miError)
    
    
    def cons4(self):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT Adultos.Nombre, Adultos.Apellido FROM Adultos INNER JOIN Inscripcion ON Adultos.idAdulto = Inscripcion.IdAdulto WHERE Inscripcion.IdActividad = 2;"
            mycursor.execute(query)
            resultados = mycursor.fetchall()
            
            tabla_resultados = []
            for registro in resultados:
                tabla_resultados.append([registro[0], registro[1]])
            
            headers = ["Nombre", "Apellido"]
            tabla = tabulate(tabla_resultados, headers, tablefmt="pretty")
            
            QMessageBox.information(self,"• Listado de Inscritos en Actividad",tabla)
            mycursor.close()
        except Exception as miError:
            print("Fallo ejecutando el procedimiento..!!")
            print(miError)
    
    
    def cons5(self):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT Actividades.Fecha, Actividades.Nombre, Inscripcion.Calificacion FROM Actividades INNER JOIN Inscripcion ON Actividades.idActividad = Inscripcion.IdActividad INNER JOIN Adultos ON Adultos.idAdulto = Inscripcion.IdAdulto WHERE Adultos.idAdulto = 4444;"
            mycursor.execute(query)
            resultados = mycursor.fetchall()
            
            tabla_resultados = []
            for registro in resultados:
                tabla_resultados.append([registro[0], registro[1], registro[2]])
            
            headers = ["Fecha", "Actividad", "Calificacion"]
            tabla = tabulate(tabla_resultados, headers, tablefmt="pretty")
            
            QMessageBox.information(self,"Actividades realizadas",tabla)
            mycursor.close()
        except Exception as miError:
            print("Fallo ejecutando el procedimiento..!!")
            print(miError)
            
    def cons6(self):
        try:
            mycursor = self.miConexion.cursor()
            query = "SELECT c.Nombre AS Centro, a.Nombre AS Actividad FROM Centros c LEFT JOIN Actividades a ON c.Nombre = a.Centro WHERE a.Nombre IS NOT NULL;"
            mycursor.execute(query)
            resultados = mycursor.fetchall()
            
            tabla_resultados = []
            for registro in resultados:
                tabla_resultados.append([registro[0], registro[1]])
            
            headers = ["Centro", "Actividad"]
            tabla = tabulate(tabla_resultados, headers, tablefmt="pretty")
            
            QMessageBox.information(self,"Actividades por Centro",tabla)
            mycursor.close()
        except Exception as miError:
            print("Fallo ejecutando el procedimiento..!!")
            print(miError)
    
    def cerrar(self):
        self.con.desconectar()
        self.close()
 
if __name__ == '__main__':
	app =QApplication([])
	ventanaPrincipal = Principal()
	ventanaPrincipal.show()
	sys.exit(app.exec())
