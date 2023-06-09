# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Autoaligner
                                 A QGIS plugin
 Auto align plugin based on Ola and Łukasz solution
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-04-27
        copyright            : (C) 2023 by na
        email                : na
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Autoaligner class from file Autoaligner.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .auto_aligner import Autoaligner
    return Autoaligner(iface)
