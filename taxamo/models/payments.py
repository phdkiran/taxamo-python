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
class Payments:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'amount': 'number',
            'payment_timestamp': 'str',
            'payment_information': 'str'

        }


        #Amount that has been paid. Use negative value to register refunds.
        self.amount = None # number
        #When the payment was received in yyyy-MM-dd HH:mm:ss (24 hour format, UTC+0 timezone).
        self.payment_timestamp = None # str
        #Additional payment information.
        self.payment_information = None # str
        
