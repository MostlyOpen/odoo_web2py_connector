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

db = DAL('sqlite://storage.sqlite', pool_size=1, check_reserved=['all'])

db.define_table('file_set',
                Field('file_name'),
                Field('file_date', 'date'),
                Field('files', 'list:reference arquivos')
                )

db.file_set.files.requires = IS_IN_DB(db, 'uploaded_files.id', 'uploaded_files.uploaded_file', multiple=True)

db.define_table('uploaded_files', 
                Field('uploaded_file', 'upload', autodelete=True)
                )
