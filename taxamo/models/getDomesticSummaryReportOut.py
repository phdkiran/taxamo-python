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
class GetDomesticSummaryReportOut:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'end_date': 'str',
            'domestic_refunds_amount': 'number',
            'currency_code': 'str',
            'global_refunds_tax_amount': 'number',
            'domestic_refunds_tax_amount': 'number',
            'eu_tax_deducted_refunds': 'number',
            'global_sales_amount': 'number',
            'global_refunds_amount': 'number',
            'global_sales_tax_amount': 'number',
            'eu_tax_deducted_sales': 'number',
            'start_date': 'str',
            'domestic_tax_amount': 'number',
            'domestic_sales_amount': 'number'

        }


        #Period end date in yyyy-MM-dd'T'hh:mm:ss'Z' format.
        self.end_date = None # str
        #Domestic sales refunds amount.
        self.domestic_refunds_amount = None # number
        #Three-letter ISO currency code.
        self.currency_code = None # str
        #Global sales refunds amount. This includes refunds from domestic country too.
        self.global_refunds_tax_amount = None # number
        #Domestic sales refunds tax amout.
        self.domestic_refunds_tax_amount = None # number
        #EU deducted tax sales.
        self.eu_tax_deducted_refunds = None # number
        #Global sales amount. This includes sales from domestic country too.
        self.global_sales_amount = None # number
        #Global sales refunds amount. This includes refunds from domestic country too.
        self.global_refunds_amount = None # number
        #Global sales amount. This includes sales from domestic country too.
        self.global_sales_tax_amount = None # number
        #EU deducted tax sales.
        self.eu_tax_deducted_sales = None # number
        #Period start date in yyyy-MM-dd'T'hh:mm:ss'Z' format.
        self.start_date = None # str
        #Domestic sales tax amout.
        self.domestic_tax_amount = None # number
        #Domestic sales amount.
        self.domestic_sales_amount = None # number
        
