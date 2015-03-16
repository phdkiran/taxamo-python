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
class Transaction:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'invoice_date': 'str',
            'invoice_address': 'invoice_address',
            'buyer_tax_number_valid': 'bool',
            'manual': 'bool',
            'buyer_credit_card_prefix': 'str',
            'custom_fields': 'list[custom_fields]',
            'additional_currencies': 'additional_currencies',
            'buyer_tax_number': 'str',
            'custom_id': 'str',
            'deducted_tax_amount': 'number',
            'tax_country_code': 'str',
            'force_country_code': 'str',
            'tax_amount': 'number',
            'tax_timezone': 'str',
            'buyer_email': 'str',
            'original_transaction_key': 'str',
            'test': 'bool',
            'status': 'str',
            'create_timestamp': 'str',
            'total_amount': 'number',
            'tax_entity_name': 'str',
            'buyer_ip': 'str',
            'refunded_tax_amount': 'number',
            'countries': 'countries',
            'invoice_place': 'str',
            'verification_token': 'str',
            'tax_deducted': 'bool',
            'buyer_name': 'str',
            'confirm_timestamp': 'str',
            'evidence': 'evidence',
            'amount': 'number',
            'custom_data': 'str',
            'billing_country_code': 'str',
            'tax_supported': 'bool',
            'invoice_number': 'str',
            'currency_code': 'str',
            'refunded_total_amount': 'number',
            'description': 'str',
            'supply_date': 'str',
            'transaction_lines': 'list[transaction_lines]',
            'order_date': 'str',
            'key': 'str'

        }


        #Invoice date of issue.
        self.invoice_date = None # str
        #Invoice address.
        self.invoice_address = None # invoice_address
        #If the buyer tax number has been provided and was validated successfully.
        self.buyer_tax_number_valid = None # bool
        #Is the transaction created manually - using private token. In manual mode, it is the merchant who calculates tax country and validates evidence. If you need API to do that when accessing the API with private token, just skip the 'manual' flag or use false value there and provide customer's ip address through buyer_ip field.
        self.manual = None # bool
        #Buyer's credit card prefix.
        self.buyer_credit_card_prefix = None # str
        #Custom fields, stored as key-value pairs. This property is not processed and used mostly with Taxamo-built helpers.
        self.custom_fields = None # list[custom_fields]
        #Additional currency information - can be used to receive additional information about invoice in another currency.
        self.additional_currencies = None # additional_currencies
        # Buyer's tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly.
        self.buyer_tax_number = None # str
        #Custom identifier provided upon transaction creation.
        self.custom_id = None # str
        #How much tax has been deducted.
        self.deducted_tax_amount = None # number
        #Two-letter ISO country code, e.g. FR. This code applies to detected/set country for transaction, but can be set using manual mode.
        self.tax_country_code = None # str
        #Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation.
        self.force_country_code = None # str
        #Tax amount of transaction.
        self.tax_amount = None # number
        #Timezone name for tax transaction.
        self.tax_timezone = None # str
        #Buyer's declared email address.
        self.buyer_email = None # str
        #Use data and evidence from original transaction. Tax will be re-calculated, but evidence won't be re-checked.
        self.original_transaction_key = None # str
        #Was this transaction created in test mode?
        self.test = None # bool
        #Transaction status.
        self.status = None # str
        #Date and time of transaction creation.
        self.create_timestamp = None # str
        #Total amount of transaction.
        self.total_amount = None # number
        #To which entity is the tax due.
        self.tax_entity_name = None # str
        #IP address of the buyer in dotted decimal (IPv4) or text format (IPv6).
        self.buyer_ip = None # str
        #Refunded tax amount.
        self.refunded_tax_amount = None # number
        #Map of countries calculated from evidence provided. This value is not stored and is available only upon tax calculation.
        self.countries = None # countries
        #Invoice place of issue.
        self.invoice_place = None # str
        #Verification token
        self.verification_token = None # str
        #If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example.
        self.tax_deducted = None # bool
        #Buyer's name - first name and last name or company name.
        self.buyer_name = None # str
        #Date and time of transaction confirmation.
        self.confirm_timestamp = None # str
        #Tax country of residence evidence.
        self.evidence = None # evidence
        #Amount of transaction without tax.
        self.amount = None # number
        #Custom data related to transaction.
        self.custom_data = None # str
        #Billing two letter ISO country code.
        self.billing_country_code = None # str
        #Is tax calculation supported for a detected tax location?
        self.tax_supported = None # bool
        #Invoice number.
        self.invoice_number = None # str
        #Currency code for transaction - e.g. EUR.
        self.currency_code = None # str
        #Total amount refunde (including tax).
        self.refunded_total_amount = None # number
        #Transaction description.
        self.description = None # str
        #Supply date in yyyy-MM-dd format.
        self.supply_date = None # str
        #Transaction lines.
        self.transaction_lines = None # list[transaction_lines]
        #Order date in yyyy-MM-dd format, in merchant's timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time. When using public token, the default value is used.
        self.order_date = None # str
        #Id generated by taxamo.
        self.key = None # str
        
