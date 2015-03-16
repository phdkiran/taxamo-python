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
class ValidateTaxNumberOut:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'tax_deducted': 'bool',
            'buyer_tax_number': 'str',
            'buyer_tax_number_valid': 'bool',
            'billing_country_code': 'str'

        }


        #If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example.
        self.tax_deducted = None # bool
        # Buyer's tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly.
        self.buyer_tax_number = None # str
        #If the buyer tax number has been provided and was validated successfully.
        self.buyer_tax_number_valid = None # bool
        #Billing two letter ISO country code.
        self.billing_country_code = None # str
        
