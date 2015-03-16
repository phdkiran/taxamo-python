#!/usr/bin/env python
"""
Copyright 2014-2015 Taxamo, Ltd.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class Summary:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'quarter': 'str',
            'tax_amount': 'number',
            'currency_code': 'str',
            'indicative': 'bool',
            'fx_rate_date': 'str',
            'tax_entity_name': 'str'

        }


        #Quarter that this summary applies to.
        self.quarter = None # str
        #Tax amount due in this quarter.
        self.tax_amount = None # number
        #In which currency code the settlement was calculated.
        self.currency_code = None # str
        #If the quarter isn't closed yet, tax amount is indicative, as we cannot determine FX rate or all transactions yet.
        self.indicative = None # bool
        #Date of ECB FX rate used for conversions in yyyy-MM-dd'T'hh:mm:ss'Z' format.
        self.fx_rate_date = None # str
        #Tax entity that the tax is due.
        self.tax_entity_name = None # str
        
