# -*- coding: utf-8 -*-
##############################################################################
#
#    Author Joel Grand-Guillaume. Copyright 2012 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'Account Constraints',
    'version' : '1.0',
    'depends' : [
                 'account',
                 ],
    'author' : 'Camptocamp',
    'license': 'AGPL-3',
    'category': 'Generic Modules/Accounting',
    'description': """
Account Constraints
===================

Add constraints in the accounting module of OpenERP to avoid bad usage
by users that lead to corrupted datas. This is based on our experiences
and legal state of the art in other software.

Summary of constraints are:

* Add a constraint on account move: you cannot pickup a date that is not
  in the fiscal year of the concerned period

* For manual entries when multicurrency:

  a. Validation on the use of the 'Currency' and 'Currency Amount'
     fields as it is possible to enter one without the other
  b. Validation to prevent a Credit amount with a positive
     'Currency Amount', or a Debit with a negative 'Currency Amount'

* Add a check on entries that user cannot provide a secondary currency
  if the same than the company one.

    """,
    'website': 'http://www.camptocamp.com',
    'data': [],
    'installable': True,
}