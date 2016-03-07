# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2016-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################


def index():
    response.flash = T("Odoo web2py Connector - Uploaded Files")
    grid = SQLFORM.grid(db.file_set, user_signature=False)
    return dict(message=H2('Uploaded Files'), grid=grid)


def upload_file():
    try:
        id = db.uploaded_files.insert(uploaded_file=db.uploaded_files.uploaded_file.store(request.vars.file, request.vars.filename))
        return id
    except:
        return dict(message=T('Upload error!'))


def delete_file():
    try:
        name = request.args[0]
        db(db.uploaded_files.uploaded_file == name).delete()
        return name
    except:
        return dict(message=T('Delete error!'))
