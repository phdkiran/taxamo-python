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
class Report:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'tax_rate': 'number',
            'amount': 'number',
            'country_name': 'str',
            'country_code': 'str',
            'tax_amount': 'number',
            'skip_moss': 'bool',
            'currency_code': 'str'

        }


        #Tax rate
        self.tax_rate = None # number
        #Amount w/o tax
        self.amount = None # number
        #Country name
        self.country_name = None # str
        #Two letter ISO country code.
        self.country_code = None # str
        #Tax amount
        self.tax_amount = None # number
        #If true, this line should not be entered into MOSS and is provided for informative purposes only. For example because the country is the same as MOSS registration country and merchant country.
        self.skip_moss = None # bool
        #Three-letter ISO currency code.
        self.currency_code = None # str
        
