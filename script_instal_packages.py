def function_install_module_python():
    import os
    from qgis.core import QgsApplication
    path_prefixPath=QgsApplication.prefixPath()
    path_qgis=path_prefixPath.replace('S3~1.4/apps/qgis','S 3.4').replace('/','\\')
#    directory_path_plugin=QgsApplication.qgisSettingsDirPath()
#    directory = directory_path_plugin+'python/plugins/'+folder_name_plugin+'/Install_Module_Python/'
    directory=QFileDialog.getExistingDirectory(None, 'Selection Repertoire ou se trouve le repertoire dinstallation')
    var_batchfile="""@ECHO OFF 
    set OSGEO4W_ROOT="""+path_qgis+"""
    set PATH=%OSGEO4W_ROOT%\\bin;%PATH%
    set PATH=%PATH%;%OSGEO4W_ROOT%\\apps\qgis\\bin
    @echo off
    call "%OSGEO4W_ROOT%\\bin\o4w_env.bat"
    call "%OSGEO4W_ROOT%\\bin\qt5_env.bat"
    call "%OSGEO4W_ROOT%\\bin\py3_env.bat"
    @echo off
    path %OSGEO4W_ROOT%\\apps\qgis\\bin;%PATH%
    cd /d %~dp0
    """
    with open(os.path.join(directory, 'py3-env.bat'), 'w') as OPATH:
        OPATH.writelines([var_batchfile])
    var_batch_file_name='install_pip_packages.bat'
    os.system(directory+'/'+var_batch_file_name)
function_install_module_python()