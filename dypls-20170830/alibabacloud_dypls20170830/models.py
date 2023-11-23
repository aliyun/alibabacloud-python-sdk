# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ApplyArInvoiceWithSourceRequestAddressCustomer(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        customer_id: str = None,
        customer_site: str = None,
        customer_system: str = None,
        encrypt_props: Dict[str, str] = None,
        language: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.customer_id = customer_id
        self.customer_site = customer_site
        self.customer_system = customer_system
        self.encrypt_props = encrypt_props
        self.language = language
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyArInvoiceWithSourceRequestAddress(TeaModel):
    def __init__(
        self,
        address_id: str = None,
        app_code: str = None,
        city: str = None,
        country: str = None,
        creator: str = None,
        customer: ApplyArInvoiceWithSourceRequestAddressCustomer = None,
        detailed_address: str = None,
        district: str = None,
        encrypt_props: Dict[str, str] = None,
        fixed_number: str = None,
        full_address: str = None,
        is_default: bool = None,
        is_effective: bool = None,
        language: str = None,
        mobile_number: str = None,
        province: str = None,
        recipient_name: str = None,
        related_id: str = None,
        related_system: str = None,
        sign: str = None,
        street: str = None,
        uuid: str = None,
        zip_code: str = None,
    ):
        self.address_id = address_id
        self.app_code = app_code
        self.city = city
        self.country = country
        self.creator = creator
        self.customer = customer
        self.detailed_address = detailed_address
        self.district = district
        self.encrypt_props = encrypt_props
        self.fixed_number = fixed_number
        self.full_address = full_address
        self.is_default = is_default
        self.is_effective = is_effective
        self.language = language
        self.mobile_number = mobile_number
        self.province = province
        self.recipient_name = recipient_name
        self.related_id = related_id
        self.related_system = related_system
        self.sign = sign
        self.street = street
        self.uuid = uuid
        self.zip_code = zip_code

    def validate(self):
        if self.customer:
            self.customer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_id is not None:
            result['AddressId'] = self.address_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.detailed_address is not None:
            result['DetailedAddress'] = self.detailed_address
        if self.district is not None:
            result['District'] = self.district
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.fixed_number is not None:
            result['FixedNumber'] = self.fixed_number
        if self.full_address is not None:
            result['FullAddress'] = self.full_address
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.is_effective is not None:
            result['IsEffective'] = self.is_effective
        if self.language is not None:
            result['Language'] = self.language
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.province is not None:
            result['Province'] = self.province
        if self.recipient_name is not None:
            result['RecipientName'] = self.recipient_name
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.related_system is not None:
            result['RelatedSystem'] = self.related_system
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.street is not None:
            result['Street'] = self.street
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.zip_code is not None:
            result['ZipCode'] = self.zip_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Customer') is not None:
            temp_model = ApplyArInvoiceWithSourceRequestAddressCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('DetailedAddress') is not None:
            self.detailed_address = m.get('DetailedAddress')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('FixedNumber') is not None:
            self.fixed_number = m.get('FixedNumber')
        if m.get('FullAddress') is not None:
            self.full_address = m.get('FullAddress')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('IsEffective') is not None:
            self.is_effective = m.get('IsEffective')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RecipientName') is not None:
            self.recipient_name = m.get('RecipientName')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('RelatedSystem') is not None:
            self.related_system = m.get('RelatedSystem')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Street') is not None:
            self.street = m.get('Street')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('ZipCode') is not None:
            self.zip_code = m.get('ZipCode')
        return self


class ApplyArInvoiceWithSourceRequestCustomer(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        customer_id: str = None,
        customer_site: str = None,
        customer_system: str = None,
        encrypt_props: Dict[str, str] = None,
        language: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.customer_id = customer_id
        self.customer_site = customer_site
        self.customer_system = customer_system
        self.encrypt_props = encrypt_props
        self.language = language
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyArInvoiceWithSourceRequestSourceListCustomer(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        customer_id: str = None,
        customer_site: str = None,
        customer_system: str = None,
        encrypt_props: Dict[str, str] = None,
        language: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.customer_id = customer_id
        self.customer_site = customer_site
        self.customer_system = customer_system
        self.encrypt_props = encrypt_props
        self.language = language
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyArInvoiceWithSourceRequestSourceList(TeaModel):
    def __init__(
        self,
        amount: float = None,
        app_code: str = None,
        bill_amount: float = None,
        bill_domain: str = None,
        bill_no: str = None,
        bill_type: str = None,
        blue_source_id: int = None,
        can_merge: bool = None,
        cargo_name: str = None,
        category: str = None,
        company_name: str = None,
        currency_code: str = None,
        customer: ApplyArInvoiceWithSourceRequestSourceListCustomer = None,
        discount_amount: float = None,
        discount_tax_amount: float = None,
        encrypt_props: Dict[str, str] = None,
        excluding_tax_amount: float = None,
        excluding_tax_discount_amount: float = None,
        excluding_tax_red_amount: float = None,
        excluding_tax_remain_amount: float = None,
        gmt_bill: str = None,
        gmt_bill_end: str = None,
        gmt_bill_start: str = None,
        gmt_build: str = None,
        is_apply: str = None,
        language: str = None,
        major_bill_no: str = None,
        model: str = None,
        ou_code: str = None,
        parent_category: str = None,
        product_domain: str = None,
        product_id: str = None,
        product_name: str = None,
        quantity: float = None,
        quantity_unit: str = None,
        red_amount: float = None,
        related_id: str = None,
        remain_amount: float = None,
        revenue_type: str = None,
        service_name: str = None,
        sign: str = None,
        site_id: str = None,
        source_id: int = None,
        tax_amount: float = None,
        tax_rate: float = None,
        unit_price: float = None,
        uuid: str = None,
    ):
        self.amount = amount
        self.app_code = app_code
        self.bill_amount = bill_amount
        self.bill_domain = bill_domain
        self.bill_no = bill_no
        self.bill_type = bill_type
        self.blue_source_id = blue_source_id
        self.can_merge = can_merge
        self.cargo_name = cargo_name
        self.category = category
        self.company_name = company_name
        self.currency_code = currency_code
        self.customer = customer
        self.discount_amount = discount_amount
        self.discount_tax_amount = discount_tax_amount
        self.encrypt_props = encrypt_props
        self.excluding_tax_amount = excluding_tax_amount
        self.excluding_tax_discount_amount = excluding_tax_discount_amount
        self.excluding_tax_red_amount = excluding_tax_red_amount
        self.excluding_tax_remain_amount = excluding_tax_remain_amount
        self.gmt_bill = gmt_bill
        self.gmt_bill_end = gmt_bill_end
        self.gmt_bill_start = gmt_bill_start
        self.gmt_build = gmt_build
        self.is_apply = is_apply
        self.language = language
        self.major_bill_no = major_bill_no
        self.model = model
        self.ou_code = ou_code
        self.parent_category = parent_category
        self.product_domain = product_domain
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.quantity_unit = quantity_unit
        self.red_amount = red_amount
        self.related_id = related_id
        self.remain_amount = remain_amount
        self.revenue_type = revenue_type
        self.service_name = service_name
        self.sign = sign
        self.site_id = site_id
        self.source_id = source_id
        self.tax_amount = tax_amount
        self.tax_rate = tax_rate
        self.unit_price = unit_price
        self.uuid = uuid

    def validate(self):
        if self.customer:
            self.customer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.bill_amount is not None:
            result['BillAmount'] = self.bill_amount
        if self.bill_domain is not None:
            result['BillDomain'] = self.bill_domain
        if self.bill_no is not None:
            result['BillNo'] = self.bill_no
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.blue_source_id is not None:
            result['BlueSourceId'] = self.blue_source_id
        if self.can_merge is not None:
            result['CanMerge'] = self.can_merge
        if self.cargo_name is not None:
            result['CargoName'] = self.cargo_name
        if self.category is not None:
            result['Category'] = self.category
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.discount_tax_amount is not None:
            result['DiscountTaxAmount'] = self.discount_tax_amount
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.excluding_tax_amount is not None:
            result['ExcludingTaxAmount'] = self.excluding_tax_amount
        if self.excluding_tax_discount_amount is not None:
            result['ExcludingTaxDiscountAmount'] = self.excluding_tax_discount_amount
        if self.excluding_tax_red_amount is not None:
            result['ExcludingTaxRedAmount'] = self.excluding_tax_red_amount
        if self.excluding_tax_remain_amount is not None:
            result['ExcludingTaxRemainAmount'] = self.excluding_tax_remain_amount
        if self.gmt_bill is not None:
            result['GmtBill'] = self.gmt_bill
        if self.gmt_bill_end is not None:
            result['GmtBillEnd'] = self.gmt_bill_end
        if self.gmt_bill_start is not None:
            result['GmtBillStart'] = self.gmt_bill_start
        if self.gmt_build is not None:
            result['GmtBuild'] = self.gmt_build
        if self.is_apply is not None:
            result['IsApply'] = self.is_apply
        if self.language is not None:
            result['Language'] = self.language
        if self.major_bill_no is not None:
            result['MajorBillNo'] = self.major_bill_no
        if self.model is not None:
            result['Model'] = self.model
        if self.ou_code is not None:
            result['OuCode'] = self.ou_code
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.product_domain is not None:
            result['ProductDomain'] = self.product_domain
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.quantity_unit is not None:
            result['QuantityUnit'] = self.quantity_unit
        if self.red_amount is not None:
            result['RedAmount'] = self.red_amount
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount
        if self.revenue_type is not None:
            result['RevenueType'] = self.revenue_type
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.tax_rate is not None:
            result['TaxRate'] = self.tax_rate
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('BillAmount') is not None:
            self.bill_amount = m.get('BillAmount')
        if m.get('BillDomain') is not None:
            self.bill_domain = m.get('BillDomain')
        if m.get('BillNo') is not None:
            self.bill_no = m.get('BillNo')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BlueSourceId') is not None:
            self.blue_source_id = m.get('BlueSourceId')
        if m.get('CanMerge') is not None:
            self.can_merge = m.get('CanMerge')
        if m.get('CargoName') is not None:
            self.cargo_name = m.get('CargoName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('Customer') is not None:
            temp_model = ApplyArInvoiceWithSourceRequestSourceListCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('DiscountTaxAmount') is not None:
            self.discount_tax_amount = m.get('DiscountTaxAmount')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('ExcludingTaxAmount') is not None:
            self.excluding_tax_amount = m.get('ExcludingTaxAmount')
        if m.get('ExcludingTaxDiscountAmount') is not None:
            self.excluding_tax_discount_amount = m.get('ExcludingTaxDiscountAmount')
        if m.get('ExcludingTaxRedAmount') is not None:
            self.excluding_tax_red_amount = m.get('ExcludingTaxRedAmount')
        if m.get('ExcludingTaxRemainAmount') is not None:
            self.excluding_tax_remain_amount = m.get('ExcludingTaxRemainAmount')
        if m.get('GmtBill') is not None:
            self.gmt_bill = m.get('GmtBill')
        if m.get('GmtBillEnd') is not None:
            self.gmt_bill_end = m.get('GmtBillEnd')
        if m.get('GmtBillStart') is not None:
            self.gmt_bill_start = m.get('GmtBillStart')
        if m.get('GmtBuild') is not None:
            self.gmt_build = m.get('GmtBuild')
        if m.get('IsApply') is not None:
            self.is_apply = m.get('IsApply')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MajorBillNo') is not None:
            self.major_bill_no = m.get('MajorBillNo')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OuCode') is not None:
            self.ou_code = m.get('OuCode')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ProductDomain') is not None:
            self.product_domain = m.get('ProductDomain')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('QuantityUnit') is not None:
            self.quantity_unit = m.get('QuantityUnit')
        if m.get('RedAmount') is not None:
            self.red_amount = m.get('RedAmount')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')
        if m.get('RevenueType') is not None:
            self.revenue_type = m.get('RevenueType')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('TaxRate') is not None:
            self.tax_rate = m.get('TaxRate')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyArInvoiceWithSourceRequest(TeaModel):
    def __init__(
        self,
        address: ApplyArInvoiceWithSourceRequestAddress = None,
        amount: float = None,
        app_code: str = None,
        applier: str = None,
        apply_date: str = None,
        currency_code: str = None,
        customer: ApplyArInvoiceWithSourceRequestCustomer = None,
        encrypt_props: Dict[str, str] = None,
        excluding_tax_amount: float = None,
        input_type: str = None,
        invoice_type: str = None,
        is_merged: bool = None,
        language: str = None,
        material_type: str = None,
        memo: str = None,
        ou_code: str = None,
        purchaser_bank_info: str = None,
        purchaser_contact_info: str = None,
        purchaser_name: str = None,
        purchaser_tax_no: str = None,
        request_no: str = None,
        sign: str = None,
        site_id: str = None,
        source_list: List[ApplyArInvoiceWithSourceRequestSourceList] = None,
        tax_amount: float = None,
        uuid: str = None,
    ):
        self.address = address
        self.amount = amount
        self.app_code = app_code
        self.applier = applier
        self.apply_date = apply_date
        self.currency_code = currency_code
        self.customer = customer
        self.encrypt_props = encrypt_props
        self.excluding_tax_amount = excluding_tax_amount
        self.input_type = input_type
        self.invoice_type = invoice_type
        self.is_merged = is_merged
        self.language = language
        self.material_type = material_type
        self.memo = memo
        self.ou_code = ou_code
        self.purchaser_bank_info = purchaser_bank_info
        self.purchaser_contact_info = purchaser_contact_info
        self.purchaser_name = purchaser_name
        self.purchaser_tax_no = purchaser_tax_no
        self.request_no = request_no
        self.sign = sign
        self.site_id = site_id
        self.source_list = source_list
        self.tax_amount = tax_amount
        self.uuid = uuid

    def validate(self):
        if self.address:
            self.address.validate()
        if self.customer:
            self.customer.validate()
        if self.source_list:
            for k in self.source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.applier is not None:
            result['Applier'] = self.applier
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.excluding_tax_amount is not None:
            result['ExcludingTaxAmount'] = self.excluding_tax_amount
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.is_merged is not None:
            result['IsMerged'] = self.is_merged
        if self.language is not None:
            result['Language'] = self.language
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.ou_code is not None:
            result['OuCode'] = self.ou_code
        if self.purchaser_bank_info is not None:
            result['PurchaserBankInfo'] = self.purchaser_bank_info
        if self.purchaser_contact_info is not None:
            result['PurchaserContactInfo'] = self.purchaser_contact_info
        if self.purchaser_name is not None:
            result['PurchaserName'] = self.purchaser_name
        if self.purchaser_tax_no is not None:
            result['PurchaserTaxNo'] = self.purchaser_tax_no
        if self.request_no is not None:
            result['RequestNo'] = self.request_no
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        result['SourceList'] = []
        if self.source_list is not None:
            for k in self.source_list:
                result['SourceList'].append(k.to_map() if k else None)
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = ApplyArInvoiceWithSourceRequestAddress()
            self.address = temp_model.from_map(m['Address'])
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Applier') is not None:
            self.applier = m.get('Applier')
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('Customer') is not None:
            temp_model = ApplyArInvoiceWithSourceRequestCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('ExcludingTaxAmount') is not None:
            self.excluding_tax_amount = m.get('ExcludingTaxAmount')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('IsMerged') is not None:
            self.is_merged = m.get('IsMerged')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('OuCode') is not None:
            self.ou_code = m.get('OuCode')
        if m.get('PurchaserBankInfo') is not None:
            self.purchaser_bank_info = m.get('PurchaserBankInfo')
        if m.get('PurchaserContactInfo') is not None:
            self.purchaser_contact_info = m.get('PurchaserContactInfo')
        if m.get('PurchaserName') is not None:
            self.purchaser_name = m.get('PurchaserName')
        if m.get('PurchaserTaxNo') is not None:
            self.purchaser_tax_no = m.get('PurchaserTaxNo')
        if m.get('RequestNo') is not None:
            self.request_no = m.get('RequestNo')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        self.source_list = []
        if m.get('SourceList') is not None:
            for k in m.get('SourceList'):
                temp_model = ApplyArInvoiceWithSourceRequestSourceList()
                self.source_list.append(temp_model.from_map(k))
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyArInvoiceWithSourceResponseBodyReturnValue(TeaModel):
    def __init__(
        self,
        encrypt_props: Dict[str, str] = None,
        outer_system_encrypt_str: str = None,
        outer_system_sign_str: str = None,
        sign: str = None,
    ):
        self.encrypt_props = encrypt_props
        self.outer_system_encrypt_str = outer_system_encrypt_str
        self.outer_system_sign_str = outer_system_sign_str
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.outer_system_encrypt_str is not None:
            result['OuterSystemEncryptStr'] = self.outer_system_encrypt_str
        if self.outer_system_sign_str is not None:
            result['OuterSystemSignStr'] = self.outer_system_sign_str
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('OuterSystemEncryptStr') is not None:
            self.outer_system_encrypt_str = m.get('OuterSystemEncryptStr')
        if m.get('OuterSystemSignStr') is not None:
            self.outer_system_sign_str = m.get('OuterSystemSignStr')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class ApplyArInvoiceWithSourceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        is_success: bool = None,
        return_value: ApplyArInvoiceWithSourceResponseBodyReturnValue = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.return_value = return_value

    def validate(self):
        if self.return_value:
            self.return_value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ReturnValue') is not None:
            temp_model = ApplyArInvoiceWithSourceResponseBodyReturnValue()
            self.return_value = temp_model.from_map(m['ReturnValue'])
        return self


class ApplyArInvoiceWithSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyArInvoiceWithSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyArInvoiceWithSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyBlackInfoExportRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        black_type: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.black_type = black_type
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ApplyBlackInfoExportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ApplyBlackInfoExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyBlackInfoExportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyBlackInfoExportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyCallRecordExportRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        call_date: str = None,
        call_id: str = None,
        owner_id: int = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.bill_id = bill_id
        self.call_date = call_date
        self.call_id = call_id
        self.owner_id = owner_id
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.call_date is not None:
            result['CallDate'] = self.call_date
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('CallDate') is not None:
            self.call_date = m.get('CallDate')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class ApplyCallRecordExportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ApplyCallRecordExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyCallRecordExportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyCallRecordExportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyGroupNumberExportRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        owner_id: int = None,
        pool_key: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.group_id = group_id
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ApplyGroupNumberExportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ApplyGroupNumberExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyGroupNumberExportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyGroupNumberExportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyRingToneRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        id: str = None,
        owner_id: int = None,
        play_type: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.id = id
        self.owner_id = owner_id
        self.play_type = play_type
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_type is not None:
            result['PlayType'] = self.play_type
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayType') is not None:
            self.play_type = m.get('PlayType')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ApplyRingToneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ApplyRingToneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyRingToneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyRingToneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchOccupySecretResRequestBatchOccupyList(TeaModel):
    def __init__(
        self,
        count: int = None,
        order_detail_id: int = None,
        order_id: int = None,
        partner_key: str = None,
        res_type: int = None,
        secret_no_type: int = None,
    ):
        self.count = count
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.partner_key = partner_key
        self.res_type = res_type
        self.secret_no_type = secret_no_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.order_detail_id is not None:
            result['OrderDetailId'] = self.order_detail_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_key is not None:
            result['PartnerKey'] = self.partner_key
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.secret_no_type is not None:
            result['SecretNoType'] = self.secret_no_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('OrderDetailId') is not None:
            self.order_detail_id = m.get('OrderDetailId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerKey') is not None:
            self.partner_key = m.get('PartnerKey')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('SecretNoType') is not None:
            self.secret_no_type = m.get('SecretNoType')
        return self


class BatchOccupySecretResRequest(TeaModel):
    def __init__(
        self,
        batch_occupy_list: List[BatchOccupySecretResRequestBatchOccupyList] = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.batch_occupy_list = batch_occupy_list
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.batch_occupy_list:
            for k in self.batch_occupy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BatchOccupyList'] = []
        if self.batch_occupy_list is not None:
            for k in self.batch_occupy_list:
                result['BatchOccupyList'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_occupy_list = []
        if m.get('BatchOccupyList') is not None:
            for k in m.get('BatchOccupyList'):
                temp_model = BatchOccupySecretResRequestBatchOccupyList()
                self.batch_occupy_list.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class BatchOccupySecretResShrinkRequest(TeaModel):
    def __init__(
        self,
        batch_occupy_list_shrink: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.batch_occupy_list_shrink = batch_occupy_list_shrink
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_occupy_list_shrink is not None:
            result['BatchOccupyList'] = self.batch_occupy_list_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchOccupyList') is not None:
            self.batch_occupy_list_shrink = m.get('BatchOccupyList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class BatchOccupySecretResResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchOccupySecretResResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchOccupySecretResResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchOccupySecretResResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindResourceRequest(TeaModel):
    def __init__(
        self,
        asr_model_id: str = None,
        asr_status: bool = None,
        axn_extension_b: str = None,
        bill_id: str = None,
        exp_time: str = None,
        is_record: bool = None,
        owner_id: int = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.asr_model_id = asr_model_id
        self.asr_status = asr_status
        self.axn_extension_b = axn_extension_b
        self.bill_id = bill_id
        self.exp_time = exp_time
        self.is_record = is_record
        self.owner_id = owner_id
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id
        if self.asr_status is not None:
            result['AsrStatus'] = self.asr_status
        if self.axn_extension_b is not None:
            result['AxnExtensionB'] = self.axn_extension_b
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.exp_time is not None:
            result['ExpTime'] = self.exp_time
        if self.is_record is not None:
            result['IsRecord'] = self.is_record
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')
        if m.get('AsrStatus') is not None:
            self.asr_status = m.get('AsrStatus')
        if m.get('AxnExtensionB') is not None:
            self.axn_extension_b = m.get('AxnExtensionB')
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('ExpTime') is not None:
            self.exp_time = m.get('ExpTime')
        if m.get('IsRecord') is not None:
            self.is_record = m.get('IsRecord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class BindResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class BindResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BlackOperateRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        black_map: str = None,
        black_type: str = None,
        operate_type: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.black_map = black_map
        self.black_type = black_type
        self.operate_type = operate_type
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.black_map is not None:
            result['BlackMap'] = self.black_map
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BlackMap') is not None:
            self.black_map = m.get('BlackMap')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class BlackOperateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class BlackOperateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BlackOperateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BlackOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertifyInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        phone_no: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.phone_no = phone_no
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateCertifyInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateCertifyInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCertifyInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCertifyInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateContactsRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        name: str = None,
        owner_id: int = None,
        phone_number: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.name = name
        self.owner_id = owner_id
        self.phone_number = phone_number
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateContactsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateContactsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupDetailRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        number_list: str = None,
        owner_id: int = None,
        pool_key: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.group_id = group_id
        self.number_list = number_list
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.number_list is not None:
            result['NumberList'] = self.number_list
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateGroupDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGroupDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupInfoRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        number_list: str = None,
        owner_id: int = None,
        pool_key: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.name = name
        self.number_list = number_list
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.number_list is not None:
            result['NumberList'] = self.number_list
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateGroupInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateGroupInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGroupInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGroupInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogicalDeleteRequest(TeaModel):
    def __init__(
        self,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        message: str = None,
        pk: str = None,
        prod_code: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
    ):
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.message = message
        self.pk = pk
        self.prod_code = prod_code
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        return self


class CreateLogicalDeleteResponseBody(TeaModel):
    def __init__(
        self,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        message: str = None,
        pk: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
    ):
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.message = message
        self.pk = pk
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        return self


class CreateLogicalDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLogicalDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLogicalDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMessageCallbackRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        callback_url: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.biz_type = biz_type
        self.callback_url = callback_url
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateMessageCallbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateMessageCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMessageCallbackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMessageCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMessageQueueRequest(TeaModel):
    def __init__(
        self,
        bill_ids: str = None,
        biz_type: str = None,
        owner_id: int = None,
        prod_code: str = None,
        queue_name: str = None,
        queue_title: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_ids = bill_ids
        self.biz_type = biz_type
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.queue_name = queue_name
        self.queue_title = queue_title
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_ids is not None:
            result['BillIds'] = self.bill_ids
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.queue_title is not None:
            result['QueueTitle'] = self.queue_title
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillIds') is not None:
            self.bill_ids = m.get('BillIds')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('QueueTitle') is not None:
            self.queue_title = m.get('QueueTitle')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateMessageQueueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateMessageQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMessageQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMessageQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePhysicalDeleteRequest(TeaModel):
    def __init__(
        self,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        message: str = None,
        pk: str = None,
        prod_code: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
    ):
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.message = message
        self.pk = pk
        self.prod_code = prod_code
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        return self


class CreatePhysicalDeleteResponseBody(TeaModel):
    def __init__(
        self,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        message: str = None,
        pk: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
    ):
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.message = message
        self.pk = pk
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        return self


class CreatePhysicalDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePhysicalDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePhysicalDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePoolInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        pool_name: str = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.pool_name = pool_name
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreatePoolInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreatePoolInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePoolInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePoolInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        prod_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.prod_id = prod_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.prod_id is not None:
            result['ProdId'] = self.prod_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ProdId') is not None:
            self.prod_id = m.get('ProdId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRingToneRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        file_key: str = None,
        owner_id: int = None,
        play_type: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ring_name: str = None,
        tts: str = None,
    ):
        self.bill_id = bill_id
        self.file_key = file_key
        self.owner_id = owner_id
        self.play_type = play_type
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.ring_name = ring_name
        self.tts = tts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_type is not None:
            result['PlayType'] = self.play_type
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ring_name is not None:
            result['RingName'] = self.ring_name
        if self.tts is not None:
            result['Tts'] = self.tts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayType') is not None:
            self.play_type = m.get('PlayType')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RingName') is not None:
            self.ring_name = m.get('RingName')
        if m.get('Tts') is not None:
            self.tts = m.get('Tts')
        return self


class CreateRingToneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateRingToneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRingToneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRingToneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubsTrialRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        phone_a: str = None,
        phone_b: str = None,
        prod_code: str = None,
        res_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.phone_a = phone_a
        self.phone_b = phone_b
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_a is not None:
            result['PhoneA'] = self.phone_a
        if self.phone_b is not None:
            result['PhoneB'] = self.phone_b
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneA') is not None:
            self.phone_a = m.get('PhoneA')
        if m.get('PhoneB') is not None:
            self.phone_b = m.get('PhoneB')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateSubsTrialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateSubsTrialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSubsTrialResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSubsTrialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransferRecordRequest(TeaModel):
    def __init__(
        self,
        city: str = None,
        number_list: str = None,
        origin_bill_id: str = None,
        origin_name: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        target_bill_id: str = None,
        target_name: str = None,
        total: int = None,
        transfer_type: int = None,
    ):
        self.city = city
        self.number_list = number_list
        self.origin_bill_id = origin_bill_id
        self.origin_name = origin_name
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.target_bill_id = target_bill_id
        self.target_name = target_name
        self.total = total
        self.transfer_type = transfer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.number_list is not None:
            result['NumberList'] = self.number_list
        if self.origin_bill_id is not None:
            result['OriginBillId'] = self.origin_bill_id
        if self.origin_name is not None:
            result['OriginName'] = self.origin_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.target_bill_id is not None:
            result['TargetBillId'] = self.target_bill_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.total is not None:
            result['Total'] = self.total
        if self.transfer_type is not None:
            result['TransferType'] = self.transfer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')
        if m.get('OriginBillId') is not None:
            self.origin_bill_id = m.get('OriginBillId')
        if m.get('OriginName') is not None:
            self.origin_name = m.get('OriginName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TargetBillId') is not None:
            self.target_bill_id = m.get('TargetBillId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')
        return self


class CreateTransferRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateTransferRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTransferRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransferRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCertifyInfoRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.certify_id = certify_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteCertifyInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteCertifyInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCertifyInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCertifyInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContactsRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        id: int = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.id = id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteContactsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteContactsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupDetailRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        id_list: str = None,
        owner_id: int = None,
        pool_key: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.group_id = group_id
        self.id_list = id_list
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id_list is not None:
            result['IdList'] = self.id_list
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteGroupDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGroupDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMessageCallbackRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.biz_type = biz_type
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteMessageCallbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteMessageCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMessageCallbackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteMessageCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRingToneRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.id = id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteRingToneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteRingToneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRingToneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRingToneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadCompleteRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.biz_type = biz_type
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DownloadCompleteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DownloadCompleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadCompleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DownloadCompleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportResRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        res_bind_status: int = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.res_bind_status = res_bind_status
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_bind_status is not None:
            result['ResBindStatus'] = self.res_bind_status
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResBindStatus') is not None:
            self.res_bind_status = m.get('ResBindStatus')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class ExportResResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ExportResResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportResResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExportResResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEinvoicePdfDataRequestCustomer(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        customer_id: str = None,
        customer_site: str = None,
        customer_system: str = None,
        encrypt_props: Dict[str, str] = None,
        language: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.customer_id = customer_id
        self.customer_site = customer_site
        self.customer_system = customer_system
        self.encrypt_props = encrypt_props
        self.language = language
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetEinvoicePdfDataRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        customer: GetEinvoicePdfDataRequestCustomer = None,
        encrypt_props: Dict[str, str] = None,
        invoice_code: str = None,
        invoice_no: str = None,
        language: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.customer = customer
        self.encrypt_props = encrypt_props
        self.invoice_code = invoice_code
        self.invoice_no = invoice_no
        self.language = language
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        if self.customer:
            self.customer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Customer') is not None:
            temp_model = GetEinvoicePdfDataRequestCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetEinvoicePdfDataResponseBodyReturnValue(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        einvoice_data: List[int] = None,
        encrypt_props: Dict[str, str] = None,
        invoice_code: str = None,
        invoice_no: str = None,
        language: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.einvoice_data = einvoice_data
        self.encrypt_props = encrypt_props
        self.invoice_code = invoice_code
        self.invoice_no = invoice_no
        self.language = language
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.einvoice_data is not None:
            result['EInvoiceData'] = self.einvoice_data
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('EInvoiceData') is not None:
            self.einvoice_data = m.get('EInvoiceData')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetEinvoicePdfDataResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        is_success: bool = None,
        return_value: GetEinvoicePdfDataResponseBodyReturnValue = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.return_value = return_value

    def validate(self):
        if self.return_value:
            self.return_value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ReturnValue') is not None:
            temp_model = GetEinvoicePdfDataResponseBodyReturnValue()
            self.return_value = temp_model.from_map(m['ReturnValue'])
        return self


class GetEinvoicePdfDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEinvoicePdfDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEinvoicePdfDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretAsrInfoRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        call_time: str = None,
        pool_key: str = None,
        prod_code: str = None,
    ):
        self.call_id = call_id
        self.call_time = call_time
        self.pool_key = pool_key
        self.prod_code = prod_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        return self


class GetSecretAsrInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        channel: str = None,
        text: str = None,
    ):
        self.channel = channel
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetSecretAsrInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetSecretAsrInfoResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSecretAsrInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSecretAsrInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSecretAsrInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSecretAsrInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserResourceTagStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetUserResourceTagStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResourceTagStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResourceTagStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserResourceTagStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsrLanguageModelsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListAsrLanguageModelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAsrLanguageModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAsrLanguageModelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAsrLanguageModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockResourceRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class LockResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class LockResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LockResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LockResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OccupySecretResRequest(TeaModel):
    def __init__(
        self,
        city: str = None,
        is_display_pool: bool = None,
        no_like: str = None,
        order_detail_id: int = None,
        order_id: int = None,
        owner_id: int = None,
        partner_key: str = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no_type: int = None,
        total_count: int = None,
        secret_no: str = None,
    ):
        self.city = city
        self.is_display_pool = is_display_pool
        self.no_like = no_like
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.owner_id = owner_id
        self.partner_key = partner_key
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no_type = secret_no_type
        self.total_count = total_count
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.is_display_pool is not None:
            result['IsDisplayPool'] = self.is_display_pool
        if self.no_like is not None:
            result['NoLike'] = self.no_like
        if self.order_detail_id is not None:
            result['OrderDetailId'] = self.order_detail_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.partner_key is not None:
            result['PartnerKey'] = self.partner_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no_type is not None:
            result['SecretNoType'] = self.secret_no_type
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.secret_no is not None:
            result['secretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('IsDisplayPool') is not None:
            self.is_display_pool = m.get('IsDisplayPool')
        if m.get('NoLike') is not None:
            self.no_like = m.get('NoLike')
        if m.get('OrderDetailId') is not None:
            self.order_detail_id = m.get('OrderDetailId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PartnerKey') is not None:
            self.partner_key = m.get('PartnerKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNoType') is not None:
            self.secret_no_type = m.get('SecretNoType')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('secretNo') is not None:
            self.secret_no = m.get('secretNo')
        return self


class OccupySecretResResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OccupySecretResResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OccupySecretResResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OccupySecretResResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OrderSucceededCallbackRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        data: str = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class OrderSucceededCallbackResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class OrderSucceededCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OrderSucceededCallbackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OrderSucceededCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PoolConfigRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        callback_type: int = None,
        frozen_day: int = None,
        need_all_call_records: bool = None,
        open_sms_white: bool = None,
        owner_id: int = None,
        pool_warning_limit: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        select_xmode: str = None,
        smart_sms_whitelist: str = None,
        sms_channel: str = None,
    ):
        self.bill_id = bill_id
        self.callback_type = callback_type
        self.frozen_day = frozen_day
        self.need_all_call_records = need_all_call_records
        self.open_sms_white = open_sms_white
        self.owner_id = owner_id
        self.pool_warning_limit = pool_warning_limit
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.select_xmode = select_xmode
        self.smart_sms_whitelist = smart_sms_whitelist
        self.sms_channel = sms_channel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.callback_type is not None:
            result['CallbackType'] = self.callback_type
        if self.frozen_day is not None:
            result['FrozenDay'] = self.frozen_day
        if self.need_all_call_records is not None:
            result['NeedAllCallRecords'] = self.need_all_call_records
        if self.open_sms_white is not None:
            result['OpenSmsWhite'] = self.open_sms_white
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_warning_limit is not None:
            result['PoolWarningLimit'] = self.pool_warning_limit
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.select_xmode is not None:
            result['SelectXMode'] = self.select_xmode
        if self.smart_sms_whitelist is not None:
            result['SmartSmsWhitelist'] = self.smart_sms_whitelist
        if self.sms_channel is not None:
            result['SmsChannel'] = self.sms_channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('CallbackType') is not None:
            self.callback_type = m.get('CallbackType')
        if m.get('FrozenDay') is not None:
            self.frozen_day = m.get('FrozenDay')
        if m.get('NeedAllCallRecords') is not None:
            self.need_all_call_records = m.get('NeedAllCallRecords')
        if m.get('OpenSmsWhite') is not None:
            self.open_sms_white = m.get('OpenSmsWhite')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolWarningLimit') is not None:
            self.pool_warning_limit = m.get('PoolWarningLimit')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SelectXMode') is not None:
            self.select_xmode = m.get('SelectXMode')
        if m.get('SmartSmsWhitelist') is not None:
            self.smart_sms_whitelist = m.get('SmartSmsWhitelist')
        if m.get('SmsChannel') is not None:
            self.sms_channel = m.get('SmsChannel')
        return self


class PoolConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class PoolConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PoolConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PoolConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurchaseResourcesRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        buy_number: int = None,
        is_display_pool: bool = None,
        no_like: str = None,
        owner_id: int = None,
        prod_code: str = None,
        region_name: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spec_id: int = None,
        usage_scenarios: str = None,
    ):
        self.bill_id = bill_id
        self.buy_number = buy_number
        self.is_display_pool = is_display_pool
        self.no_like = no_like
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.region_name = region_name
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.spec_id = spec_id
        self.usage_scenarios = usage_scenarios

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.buy_number is not None:
            result['BuyNumber'] = self.buy_number
        if self.is_display_pool is not None:
            result['IsDisplayPool'] = self.is_display_pool
        if self.no_like is not None:
            result['NoLike'] = self.no_like
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.usage_scenarios is not None:
            result['UsageScenarios'] = self.usage_scenarios
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BuyNumber') is not None:
            self.buy_number = m.get('BuyNumber')
        if m.get('IsDisplayPool') is not None:
            self.is_display_pool = m.get('IsDisplayPool')
        if m.get('NoLike') is not None:
            self.no_like = m.get('NoLike')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('UsageScenarios') is not None:
            self.usage_scenarios = m.get('UsageScenarios')
        return self


class PurchaseResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class PurchaseResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PurchaseResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PurchaseResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBindingDetailsRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
        sub_id: str = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no
        self.sub_id = sub_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.sub_id is not None:
            result['SubId'] = self.sub_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')
        return self


class QueryBindingDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryBindingDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBindingDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBindingDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBlackListRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        black_prefix: str = None,
        black_type: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.black_prefix = black_prefix
        self.black_type = black_type
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.black_prefix is not None:
            result['BlackPrefix'] = self.black_prefix
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BlackPrefix') is not None:
            self.black_prefix = m.get('BlackPrefix')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryBlackListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBlackListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBuyPageInitDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryBuyPageInitDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryBuyPageInitDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBuyPageInitDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBuyPageInitDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBuyPageResCountRequest(TeaModel):
    def __init__(
        self,
        city: str = None,
        like: str = None,
        owner_id: int = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spec_id: int = None,
    ):
        self.city = city
        self.like = like
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.spec_id = spec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.like is not None:
            result['Like'] = self.like
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class QueryBuyPageResCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryBuyPageResCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBuyPageResCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBuyPageResCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBuyPageResInfoRequest(TeaModel):
    def __init__(
        self,
        like: str = None,
        owner_id: int = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spec_id: int = None,
    ):
        self.like = like
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.spec_id = spec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.like is not None:
            result['Like'] = self.like
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class QueryBuyPageResInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryBuyPageResInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBuyPageResInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBuyPageResInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBuyResInfoRequest(TeaModel):
    def __init__(
        self,
        like: str = None,
        owner_id: int = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spec_id: int = None,
    ):
        self.like = like
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.spec_id = spec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.like is not None:
            result['Like'] = self.like
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class QueryBuyResInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryBuyResInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBuyResInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBuyResInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallRecordingListRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        call_date: str = None,
        call_id: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.bill_id = bill_id
        self.call_date = call_date
        self.call_id = call_id
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.call_date is not None:
            result['CallDate'] = self.call_date
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('CallDate') is not None:
            self.call_date = m.get('CallDate')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class QueryCallRecordingListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryCallRecordingListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCallRecordingListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCallRecordingListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCertifyInfoListRequest(TeaModel):
    def __init__(
        self,
        certify_status: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        phone_no: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.certify_status = certify_status
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.phone_no = phone_no
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryCertifyInfoListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryCertifyInfoListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCertifyInfoListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCertifyInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCertifyOverviewInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryCertifyOverviewInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryCertifyOverviewInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCertifyOverviewInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCertifyOverviewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryContactsListRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryContactsListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryContactsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryContactsListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryContactsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCustInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryCustInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        certify_type: int = None,
        contact_phone: str = None,
        cust_id: int = None,
        cust_name: str = None,
        is_dayu_customer: bool = None,
        os_status: int = None,
        partner_id: int = None,
        user_tag: int = None,
        user_tag_2: int = None,
    ):
        self.certify_type = certify_type
        self.contact_phone = contact_phone
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.is_dayu_customer = is_dayu_customer
        self.os_status = os_status
        self.partner_id = partner_id
        self.user_tag = user_tag
        self.user_tag_2 = user_tag_2

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_type is not None:
            result['CertifyType'] = self.certify_type
        if self.contact_phone is not None:
            result['ContactPhone'] = self.contact_phone
        if self.cust_id is not None:
            result['CustId'] = self.cust_id
        if self.cust_name is not None:
            result['CustName'] = self.cust_name
        if self.is_dayu_customer is not None:
            result['IsDayuCustomer'] = self.is_dayu_customer
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id
        if self.user_tag is not None:
            result['UserTag'] = self.user_tag
        if self.user_tag_2 is not None:
            result['UserTag2'] = self.user_tag_2
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyType') is not None:
            self.certify_type = m.get('CertifyType')
        if m.get('ContactPhone') is not None:
            self.contact_phone = m.get('ContactPhone')
        if m.get('CustId') is not None:
            self.cust_id = m.get('CustId')
        if m.get('CustName') is not None:
            self.cust_name = m.get('CustName')
        if m.get('IsDayuCustomer') is not None:
            self.is_dayu_customer = m.get('IsDayuCustomer')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')
        if m.get('UserTag') is not None:
            self.user_tag = m.get('UserTag')
        if m.get('UserTag2') is not None:
            self.user_tag_2 = m.get('UserTag2')
        return self


class QueryCustInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: QueryCustInfoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = QueryCustInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryCustInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCustInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCustInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.biz_type = biz_type
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDownloadUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEffectiveInvoiceListByBillNosRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        bill_no: str = None,
        encrypt_props: Dict[str, str] = None,
        language: str = None,
        major_bill_no: str = None,
        ou_code: str = None,
        related_system: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.bill_no = bill_no
        self.encrypt_props = encrypt_props
        self.language = language
        self.major_bill_no = major_bill_no
        self.ou_code = ou_code
        self.related_system = related_system
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.bill_no is not None:
            result['BillNo'] = self.bill_no
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.major_bill_no is not None:
            result['MajorBillNo'] = self.major_bill_no
        if self.ou_code is not None:
            result['OuCode'] = self.ou_code
        if self.related_system is not None:
            result['RelatedSystem'] = self.related_system
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('BillNo') is not None:
            self.bill_no = m.get('BillNo')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MajorBillNo') is not None:
            self.major_bill_no = m.get('MajorBillNo')
        if m.get('OuCode') is not None:
            self.ou_code = m.get('OuCode')
        if m.get('RelatedSystem') is not None:
            self.related_system = m.get('RelatedSystem')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryEffectiveInvoiceListByBillNosResponseBodyReturnValueList(TeaModel):
    def __init__(
        self,
        ali_company: str = None,
        ali_id: int = None,
        amount: float = None,
        app_code: str = None,
        build_amount: float = None,
        category: str = None,
        encrypt_props: Dict[str, str] = None,
        invoice_no: str = None,
        invoice_status: str = None,
        invoice_title: str = None,
        language: str = None,
        order_item_no: str = None,
        parent_contract_no: str = None,
        sign: str = None,
        site: str = None,
        tax_regisger_no: str = None,
        uuid: str = None,
    ):
        self.ali_company = ali_company
        self.ali_id = ali_id
        self.amount = amount
        self.app_code = app_code
        self.build_amount = build_amount
        self.category = category
        self.encrypt_props = encrypt_props
        self.invoice_no = invoice_no
        self.invoice_status = invoice_status
        self.invoice_title = invoice_title
        self.language = language
        self.order_item_no = order_item_no
        self.parent_contract_no = parent_contract_no
        self.sign = sign
        self.site = site
        self.tax_regisger_no = tax_regisger_no
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_company is not None:
            result['AliCompany'] = self.ali_company
        if self.ali_id is not None:
            result['AliId'] = self.ali_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.build_amount is not None:
            result['BuildAmount'] = self.build_amount
        if self.category is not None:
            result['Category'] = self.category
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.invoice_status is not None:
            result['InvoiceStatus'] = self.invoice_status
        if self.invoice_title is not None:
            result['InvoiceTitle'] = self.invoice_title
        if self.language is not None:
            result['Language'] = self.language
        if self.order_item_no is not None:
            result['OrderItemNo'] = self.order_item_no
        if self.parent_contract_no is not None:
            result['ParentContractNo'] = self.parent_contract_no
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.site is not None:
            result['Site'] = self.site
        if self.tax_regisger_no is not None:
            result['TaxRegisgerNo'] = self.tax_regisger_no
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliCompany') is not None:
            self.ali_company = m.get('AliCompany')
        if m.get('AliId') is not None:
            self.ali_id = m.get('AliId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('BuildAmount') is not None:
            self.build_amount = m.get('BuildAmount')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('InvoiceStatus') is not None:
            self.invoice_status = m.get('InvoiceStatus')
        if m.get('InvoiceTitle') is not None:
            self.invoice_title = m.get('InvoiceTitle')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OrderItemNo') is not None:
            self.order_item_no = m.get('OrderItemNo')
        if m.get('ParentContractNo') is not None:
            self.parent_contract_no = m.get('ParentContractNo')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('TaxRegisgerNo') is not None:
            self.tax_regisger_no = m.get('TaxRegisgerNo')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryEffectiveInvoiceListByBillNosResponseBodyReturnValue(TeaModel):
    def __init__(
        self,
        encrypt_props: Dict[str, str] = None,
        list: List[QueryEffectiveInvoiceListByBillNosResponseBodyReturnValueList] = None,
        sign: str = None,
    ):
        self.encrypt_props = encrypt_props
        self.list = list
        self.sign = sign

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryEffectiveInvoiceListByBillNosResponseBodyReturnValueList()
                self.list.append(temp_model.from_map(k))
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class QueryEffectiveInvoiceListByBillNosResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        is_success: bool = None,
        return_value: QueryEffectiveInvoiceListByBillNosResponseBodyReturnValue = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.return_value = return_value

    def validate(self):
        if self.return_value:
            self.return_value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ReturnValue') is not None:
            temp_model = QueryEffectiveInvoiceListByBillNosResponseBodyReturnValue()
            self.return_value = temp_model.from_map(m['ReturnValue'])
        return self


class QueryEffectiveInvoiceListByBillNosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEffectiveInvoiceListByBillNosResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryEffectiveInvoiceListByBillNosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExportResUrlRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryExportResUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryExportResUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryExportResUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryExportResUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGroupDetailListRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        number: str = None,
        owner_id: int = None,
        page_no: str = None,
        page_size: str = None,
        pool_key: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.group_id = group_id
        self.number = number
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.pool_key = pool_key
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.number is not None:
            result['Number'] = self.number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryGroupDetailListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryGroupDetailListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryGroupDetailListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryGroupDetailListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGroupInfoListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: str = None,
        page_size: str = None,
        pool_key: str = None,
        prod_code: str = None,
        query_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.pool_key = pool_key
        self.prod_code = prod_code
        self.query_key = query_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.query_key is not None:
            result['QueryKey'] = self.query_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('QueryKey') is not None:
            self.query_key = m.get('QueryKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryGroupInfoListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryGroupInfoListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryGroupInfoListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryGroupInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInvoiceInfoByRequestNoRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        encrypt_props: Dict[str, str] = None,
        language: str = None,
        related_system: str = None,
        request_no: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.encrypt_props = encrypt_props
        self.language = language
        self.related_system = related_system
        self.request_no = request_no
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.related_system is not None:
            result['RelatedSystem'] = self.related_system
        if self.request_no is not None:
            result['RequestNo'] = self.request_no
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RelatedSystem') is not None:
            self.related_system = m.get('RelatedSystem')
        if m.get('RequestNo') is not None:
            self.request_no = m.get('RequestNo')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListCustomer(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        customer_id: str = None,
        customer_site: str = None,
        customer_system: str = None,
        encrypt_props: Dict[str, str] = None,
        language: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.customer_id = customer_id
        self.customer_site = customer_site
        self.customer_system = customer_system
        self.encrypt_props = encrypt_props
        self.language = language
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceListCustomer(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        customer_id: str = None,
        customer_site: str = None,
        customer_system: str = None,
        encrypt_props: Dict[str, str] = None,
        language: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.customer_id = customer_id
        self.customer_site = customer_site
        self.customer_system = customer_system
        self.encrypt_props = encrypt_props
        self.language = language
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceList(TeaModel):
    def __init__(
        self,
        amount: float = None,
        app_code: str = None,
        bill_amount: float = None,
        bill_domain: str = None,
        bill_no: str = None,
        bill_type: str = None,
        blue_source_id: int = None,
        can_merge: bool = None,
        cargo_name: str = None,
        category: str = None,
        company_name: str = None,
        currency_code: str = None,
        customer: QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceListCustomer = None,
        discount_amount: float = None,
        discount_tax_amount: float = None,
        encrypt_props: Dict[str, str] = None,
        excluding_tax_amount: float = None,
        excluding_tax_discount_amount: float = None,
        excluding_tax_red_amount: float = None,
        excluding_tax_remain_amount: float = None,
        gmt_bill: str = None,
        gmt_bill_end: str = None,
        gmt_bill_start: str = None,
        gmt_build: str = None,
        is_apply: str = None,
        language: str = None,
        major_bill_no: str = None,
        model: str = None,
        ou_code: str = None,
        parent_category: str = None,
        product_domain: str = None,
        product_id: str = None,
        product_name: str = None,
        quantity: float = None,
        quantity_unit: str = None,
        red_amount: float = None,
        related_id: str = None,
        remain_amount: float = None,
        revenue_type: str = None,
        service_name: str = None,
        sign: str = None,
        site_id: str = None,
        source_id: int = None,
        tax_amount: float = None,
        tax_rate: float = None,
        unit_price: float = None,
        uuid: str = None,
    ):
        self.amount = amount
        self.app_code = app_code
        self.bill_amount = bill_amount
        self.bill_domain = bill_domain
        self.bill_no = bill_no
        self.bill_type = bill_type
        self.blue_source_id = blue_source_id
        self.can_merge = can_merge
        self.cargo_name = cargo_name
        self.category = category
        self.company_name = company_name
        self.currency_code = currency_code
        self.customer = customer
        self.discount_amount = discount_amount
        self.discount_tax_amount = discount_tax_amount
        self.encrypt_props = encrypt_props
        self.excluding_tax_amount = excluding_tax_amount
        self.excluding_tax_discount_amount = excluding_tax_discount_amount
        self.excluding_tax_red_amount = excluding_tax_red_amount
        self.excluding_tax_remain_amount = excluding_tax_remain_amount
        self.gmt_bill = gmt_bill
        self.gmt_bill_end = gmt_bill_end
        self.gmt_bill_start = gmt_bill_start
        self.gmt_build = gmt_build
        self.is_apply = is_apply
        self.language = language
        self.major_bill_no = major_bill_no
        self.model = model
        self.ou_code = ou_code
        self.parent_category = parent_category
        self.product_domain = product_domain
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.quantity_unit = quantity_unit
        self.red_amount = red_amount
        self.related_id = related_id
        self.remain_amount = remain_amount
        self.revenue_type = revenue_type
        self.service_name = service_name
        self.sign = sign
        self.site_id = site_id
        self.source_id = source_id
        self.tax_amount = tax_amount
        self.tax_rate = tax_rate
        self.unit_price = unit_price
        self.uuid = uuid

    def validate(self):
        if self.customer:
            self.customer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.bill_amount is not None:
            result['BillAmount'] = self.bill_amount
        if self.bill_domain is not None:
            result['BillDomain'] = self.bill_domain
        if self.bill_no is not None:
            result['BillNo'] = self.bill_no
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.blue_source_id is not None:
            result['BlueSourceId'] = self.blue_source_id
        if self.can_merge is not None:
            result['CanMerge'] = self.can_merge
        if self.cargo_name is not None:
            result['CargoName'] = self.cargo_name
        if self.category is not None:
            result['Category'] = self.category
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.discount_tax_amount is not None:
            result['DiscountTaxAmount'] = self.discount_tax_amount
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.excluding_tax_amount is not None:
            result['ExcludingTaxAmount'] = self.excluding_tax_amount
        if self.excluding_tax_discount_amount is not None:
            result['ExcludingTaxDiscountAmount'] = self.excluding_tax_discount_amount
        if self.excluding_tax_red_amount is not None:
            result['ExcludingTaxRedAmount'] = self.excluding_tax_red_amount
        if self.excluding_tax_remain_amount is not None:
            result['ExcludingTaxRemainAmount'] = self.excluding_tax_remain_amount
        if self.gmt_bill is not None:
            result['GmtBill'] = self.gmt_bill
        if self.gmt_bill_end is not None:
            result['GmtBillEnd'] = self.gmt_bill_end
        if self.gmt_bill_start is not None:
            result['GmtBillStart'] = self.gmt_bill_start
        if self.gmt_build is not None:
            result['GmtBuild'] = self.gmt_build
        if self.is_apply is not None:
            result['IsApply'] = self.is_apply
        if self.language is not None:
            result['Language'] = self.language
        if self.major_bill_no is not None:
            result['MajorBillNo'] = self.major_bill_no
        if self.model is not None:
            result['Model'] = self.model
        if self.ou_code is not None:
            result['OuCode'] = self.ou_code
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.product_domain is not None:
            result['ProductDomain'] = self.product_domain
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.quantity_unit is not None:
            result['QuantityUnit'] = self.quantity_unit
        if self.red_amount is not None:
            result['RedAmount'] = self.red_amount
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount
        if self.revenue_type is not None:
            result['RevenueType'] = self.revenue_type
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.tax_rate is not None:
            result['TaxRate'] = self.tax_rate
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('BillAmount') is not None:
            self.bill_amount = m.get('BillAmount')
        if m.get('BillDomain') is not None:
            self.bill_domain = m.get('BillDomain')
        if m.get('BillNo') is not None:
            self.bill_no = m.get('BillNo')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BlueSourceId') is not None:
            self.blue_source_id = m.get('BlueSourceId')
        if m.get('CanMerge') is not None:
            self.can_merge = m.get('CanMerge')
        if m.get('CargoName') is not None:
            self.cargo_name = m.get('CargoName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('Customer') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceListCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('DiscountTaxAmount') is not None:
            self.discount_tax_amount = m.get('DiscountTaxAmount')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('ExcludingTaxAmount') is not None:
            self.excluding_tax_amount = m.get('ExcludingTaxAmount')
        if m.get('ExcludingTaxDiscountAmount') is not None:
            self.excluding_tax_discount_amount = m.get('ExcludingTaxDiscountAmount')
        if m.get('ExcludingTaxRedAmount') is not None:
            self.excluding_tax_red_amount = m.get('ExcludingTaxRedAmount')
        if m.get('ExcludingTaxRemainAmount') is not None:
            self.excluding_tax_remain_amount = m.get('ExcludingTaxRemainAmount')
        if m.get('GmtBill') is not None:
            self.gmt_bill = m.get('GmtBill')
        if m.get('GmtBillEnd') is not None:
            self.gmt_bill_end = m.get('GmtBillEnd')
        if m.get('GmtBillStart') is not None:
            self.gmt_bill_start = m.get('GmtBillStart')
        if m.get('GmtBuild') is not None:
            self.gmt_build = m.get('GmtBuild')
        if m.get('IsApply') is not None:
            self.is_apply = m.get('IsApply')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MajorBillNo') is not None:
            self.major_bill_no = m.get('MajorBillNo')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OuCode') is not None:
            self.ou_code = m.get('OuCode')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ProductDomain') is not None:
            self.product_domain = m.get('ProductDomain')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('QuantityUnit') is not None:
            self.quantity_unit = m.get('QuantityUnit')
        if m.get('RedAmount') is not None:
            self.red_amount = m.get('RedAmount')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')
        if m.get('RevenueType') is not None:
            self.revenue_type = m.get('RevenueType')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('TaxRate') is not None:
            self.tax_rate = m.get('TaxRate')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailList(TeaModel):
    def __init__(
        self,
        amount: float = None,
        app_code: str = None,
        cargo_name: str = None,
        discount_amount: float = None,
        discount_tax_amount: float = None,
        encrypt_props: Dict[str, str] = None,
        excluding_tax_amount: float = None,
        excluding_tax_discount_amount: float = None,
        excluding_tax_red_amount: float = None,
        excluding_tax_remain_amount: float = None,
        excluding_tax_unit_price: float = None,
        invoice_detail_id: int = None,
        language: str = None,
        model: str = None,
        quantity: float = None,
        quantity_unit: str = None,
        red_amount: float = None,
        related_id: str = None,
        remain_amount: float = None,
        sign: str = None,
        source_list: List[QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceList] = None,
        tax_amount: float = None,
        tax_rate: float = None,
        unit_price: float = None,
        uuid: str = None,
    ):
        self.amount = amount
        self.app_code = app_code
        self.cargo_name = cargo_name
        self.discount_amount = discount_amount
        self.discount_tax_amount = discount_tax_amount
        self.encrypt_props = encrypt_props
        self.excluding_tax_amount = excluding_tax_amount
        self.excluding_tax_discount_amount = excluding_tax_discount_amount
        self.excluding_tax_red_amount = excluding_tax_red_amount
        self.excluding_tax_remain_amount = excluding_tax_remain_amount
        self.excluding_tax_unit_price = excluding_tax_unit_price
        self.invoice_detail_id = invoice_detail_id
        self.language = language
        self.model = model
        self.quantity = quantity
        self.quantity_unit = quantity_unit
        self.red_amount = red_amount
        self.related_id = related_id
        self.remain_amount = remain_amount
        self.sign = sign
        self.source_list = source_list
        self.tax_amount = tax_amount
        self.tax_rate = tax_rate
        self.unit_price = unit_price
        self.uuid = uuid

    def validate(self):
        if self.source_list:
            for k in self.source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.cargo_name is not None:
            result['CargoName'] = self.cargo_name
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.discount_tax_amount is not None:
            result['DiscountTaxAmount'] = self.discount_tax_amount
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.excluding_tax_amount is not None:
            result['ExcludingTaxAmount'] = self.excluding_tax_amount
        if self.excluding_tax_discount_amount is not None:
            result['ExcludingTaxDiscountAmount'] = self.excluding_tax_discount_amount
        if self.excluding_tax_red_amount is not None:
            result['ExcludingTaxRedAmount'] = self.excluding_tax_red_amount
        if self.excluding_tax_remain_amount is not None:
            result['ExcludingTaxRemainAmount'] = self.excluding_tax_remain_amount
        if self.excluding_tax_unit_price is not None:
            result['ExcludingTaxUnitPrice'] = self.excluding_tax_unit_price
        if self.invoice_detail_id is not None:
            result['InvoiceDetailId'] = self.invoice_detail_id
        if self.language is not None:
            result['Language'] = self.language
        if self.model is not None:
            result['Model'] = self.model
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.quantity_unit is not None:
            result['QuantityUnit'] = self.quantity_unit
        if self.red_amount is not None:
            result['RedAmount'] = self.red_amount
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount
        if self.sign is not None:
            result['Sign'] = self.sign
        result['SourceList'] = []
        if self.source_list is not None:
            for k in self.source_list:
                result['SourceList'].append(k.to_map() if k else None)
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.tax_rate is not None:
            result['TaxRate'] = self.tax_rate
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CargoName') is not None:
            self.cargo_name = m.get('CargoName')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('DiscountTaxAmount') is not None:
            self.discount_tax_amount = m.get('DiscountTaxAmount')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('ExcludingTaxAmount') is not None:
            self.excluding_tax_amount = m.get('ExcludingTaxAmount')
        if m.get('ExcludingTaxDiscountAmount') is not None:
            self.excluding_tax_discount_amount = m.get('ExcludingTaxDiscountAmount')
        if m.get('ExcludingTaxRedAmount') is not None:
            self.excluding_tax_red_amount = m.get('ExcludingTaxRedAmount')
        if m.get('ExcludingTaxRemainAmount') is not None:
            self.excluding_tax_remain_amount = m.get('ExcludingTaxRemainAmount')
        if m.get('ExcludingTaxUnitPrice') is not None:
            self.excluding_tax_unit_price = m.get('ExcludingTaxUnitPrice')
        if m.get('InvoiceDetailId') is not None:
            self.invoice_detail_id = m.get('InvoiceDetailId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('QuantityUnit') is not None:
            self.quantity_unit = m.get('QuantityUnit')
        if m.get('RedAmount') is not None:
            self.red_amount = m.get('RedAmount')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        self.source_list = []
        if m.get('SourceList') is not None:
            for k in m.get('SourceList'):
                temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceList()
                self.source_list.append(temp_model.from_map(k))
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('TaxRate') is not None:
            self.tax_rate = m.get('TaxRate')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfoCustomer(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        customer_id: str = None,
        customer_site: str = None,
        customer_system: str = None,
        encrypt_props: Dict[str, str] = None,
        language: str = None,
        sign: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.customer_id = customer_id
        self.customer_site = customer_site
        self.customer_system = customer_system
        self.encrypt_props = encrypt_props
        self.language = language
        self.sign = sign
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfo(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        customer: QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfoCustomer = None,
        encrypt_props: Dict[str, str] = None,
        gmt_send: str = None,
        invoice_code: str = None,
        invoice_date: str = None,
        invoice_id: int = None,
        invoice_no: str = None,
        invoice_nos: str = None,
        language: str = None,
        logistics_companies: str = None,
        related_id: str = None,
        sender: str = None,
        sign: str = None,
        timestamp: int = None,
        tracking_number: str = None,
        uuid: str = None,
    ):
        self.app_code = app_code
        self.customer = customer
        self.encrypt_props = encrypt_props
        self.gmt_send = gmt_send
        self.invoice_code = invoice_code
        self.invoice_date = invoice_date
        self.invoice_id = invoice_id
        self.invoice_no = invoice_no
        self.invoice_nos = invoice_nos
        self.language = language
        self.logistics_companies = logistics_companies
        self.related_id = related_id
        self.sender = sender
        self.sign = sign
        self.timestamp = timestamp
        self.tracking_number = tracking_number
        self.uuid = uuid

    def validate(self):
        if self.customer:
            self.customer.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.gmt_send is not None:
            result['GmtSend'] = self.gmt_send
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.invoice_id is not None:
            result['InvoiceId'] = self.invoice_id
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.invoice_nos is not None:
            result['InvoiceNos'] = self.invoice_nos
        if self.language is not None:
            result['Language'] = self.language
        if self.logistics_companies is not None:
            result['LogisticsCompanies'] = self.logistics_companies
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.sender is not None:
            result['Sender'] = self.sender
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.tracking_number is not None:
            result['TrackingNumber'] = self.tracking_number
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Customer') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfoCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('GmtSend') is not None:
            self.gmt_send = m.get('GmtSend')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('InvoiceId') is not None:
            self.invoice_id = m.get('InvoiceId')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('InvoiceNos') is not None:
            self.invoice_nos = m.get('InvoiceNos')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LogisticsCompanies') is not None:
            self.logistics_companies = m.get('LogisticsCompanies')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('Sender') is not None:
            self.sender = m.get('Sender')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TrackingNumber') is not None:
            self.tracking_number = m.get('TrackingNumber')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueList(TeaModel):
    def __init__(
        self,
        amount: float = None,
        app_code: str = None,
        currency_code: str = None,
        customer: QueryInvoiceInfoByRequestNoResponseBodyReturnValueListCustomer = None,
        detail_list: List[QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailList] = None,
        encrypt_props: Dict[str, str] = None,
        excluding_tax_amount: float = None,
        excluding_tax_red_amount: float = None,
        excluding_tax_remain_amount: float = None,
        invoice_code: str = None,
        invoice_date: str = None,
        invoice_id: int = None,
        invoice_no: str = None,
        invoice_status: str = None,
        invoice_type: str = None,
        is_red: bool = None,
        is_reissue: bool = None,
        language: str = None,
        link_invoice_code: str = None,
        link_invoice_no: str = None,
        logistics_info: QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfo = None,
        material_type: str = None,
        memo: str = None,
        ou_code: str = None,
        purchaser_bank_info: str = None,
        purchaser_contact_info: str = None,
        purchaser_name: str = None,
        purchaser_tax_no: str = None,
        red_amount: float = None,
        related_id: str = None,
        remain_amount: float = None,
        sign: str = None,
        site_id: str = None,
        tax_amount: float = None,
        uuid: str = None,
    ):
        self.amount = amount
        self.app_code = app_code
        self.currency_code = currency_code
        self.customer = customer
        self.detail_list = detail_list
        self.encrypt_props = encrypt_props
        self.excluding_tax_amount = excluding_tax_amount
        self.excluding_tax_red_amount = excluding_tax_red_amount
        self.excluding_tax_remain_amount = excluding_tax_remain_amount
        self.invoice_code = invoice_code
        self.invoice_date = invoice_date
        self.invoice_id = invoice_id
        self.invoice_no = invoice_no
        self.invoice_status = invoice_status
        self.invoice_type = invoice_type
        self.is_red = is_red
        self.is_reissue = is_reissue
        self.language = language
        self.link_invoice_code = link_invoice_code
        self.link_invoice_no = link_invoice_no
        self.logistics_info = logistics_info
        self.material_type = material_type
        self.memo = memo
        self.ou_code = ou_code
        self.purchaser_bank_info = purchaser_bank_info
        self.purchaser_contact_info = purchaser_contact_info
        self.purchaser_name = purchaser_name
        self.purchaser_tax_no = purchaser_tax_no
        self.red_amount = red_amount
        self.related_id = related_id
        self.remain_amount = remain_amount
        self.sign = sign
        self.site_id = site_id
        self.tax_amount = tax_amount
        self.uuid = uuid

    def validate(self):
        if self.customer:
            self.customer.validate()
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()
        if self.logistics_info:
            self.logistics_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        result['DetailList'] = []
        if self.detail_list is not None:
            for k in self.detail_list:
                result['DetailList'].append(k.to_map() if k else None)
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.excluding_tax_amount is not None:
            result['ExcludingTaxAmount'] = self.excluding_tax_amount
        if self.excluding_tax_red_amount is not None:
            result['ExcludingTaxRedAmount'] = self.excluding_tax_red_amount
        if self.excluding_tax_remain_amount is not None:
            result['ExcludingTaxRemainAmount'] = self.excluding_tax_remain_amount
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.invoice_id is not None:
            result['InvoiceId'] = self.invoice_id
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.invoice_status is not None:
            result['InvoiceStatus'] = self.invoice_status
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.is_red is not None:
            result['IsRed'] = self.is_red
        if self.is_reissue is not None:
            result['IsReissue'] = self.is_reissue
        if self.language is not None:
            result['Language'] = self.language
        if self.link_invoice_code is not None:
            result['LinkInvoiceCode'] = self.link_invoice_code
        if self.link_invoice_no is not None:
            result['LinkInvoiceNo'] = self.link_invoice_no
        if self.logistics_info is not None:
            result['LogisticsInfo'] = self.logistics_info.to_map()
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.ou_code is not None:
            result['OuCode'] = self.ou_code
        if self.purchaser_bank_info is not None:
            result['PurchaserBankInfo'] = self.purchaser_bank_info
        if self.purchaser_contact_info is not None:
            result['PurchaserContactInfo'] = self.purchaser_contact_info
        if self.purchaser_name is not None:
            result['PurchaserName'] = self.purchaser_name
        if self.purchaser_tax_no is not None:
            result['PurchaserTaxNo'] = self.purchaser_tax_no
        if self.red_amount is not None:
            result['RedAmount'] = self.red_amount
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('Customer') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        self.detail_list = []
        if m.get('DetailList') is not None:
            for k in m.get('DetailList'):
                temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('ExcludingTaxAmount') is not None:
            self.excluding_tax_amount = m.get('ExcludingTaxAmount')
        if m.get('ExcludingTaxRedAmount') is not None:
            self.excluding_tax_red_amount = m.get('ExcludingTaxRedAmount')
        if m.get('ExcludingTaxRemainAmount') is not None:
            self.excluding_tax_remain_amount = m.get('ExcludingTaxRemainAmount')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('InvoiceId') is not None:
            self.invoice_id = m.get('InvoiceId')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('InvoiceStatus') is not None:
            self.invoice_status = m.get('InvoiceStatus')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('IsRed') is not None:
            self.is_red = m.get('IsRed')
        if m.get('IsReissue') is not None:
            self.is_reissue = m.get('IsReissue')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LinkInvoiceCode') is not None:
            self.link_invoice_code = m.get('LinkInvoiceCode')
        if m.get('LinkInvoiceNo') is not None:
            self.link_invoice_no = m.get('LinkInvoiceNo')
        if m.get('LogisticsInfo') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfo()
            self.logistics_info = temp_model.from_map(m['LogisticsInfo'])
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('OuCode') is not None:
            self.ou_code = m.get('OuCode')
        if m.get('PurchaserBankInfo') is not None:
            self.purchaser_bank_info = m.get('PurchaserBankInfo')
        if m.get('PurchaserContactInfo') is not None:
            self.purchaser_contact_info = m.get('PurchaserContactInfo')
        if m.get('PurchaserName') is not None:
            self.purchaser_name = m.get('PurchaserName')
        if m.get('PurchaserTaxNo') is not None:
            self.purchaser_tax_no = m.get('PurchaserTaxNo')
        if m.get('RedAmount') is not None:
            self.red_amount = m.get('RedAmount')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValue(TeaModel):
    def __init__(
        self,
        encrypt_props: Dict[str, str] = None,
        list: List[QueryInvoiceInfoByRequestNoResponseBodyReturnValueList] = None,
        sign: str = None,
    ):
        self.encrypt_props = encrypt_props
        self.list = list
        self.sign = sign

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueList()
                self.list.append(temp_model.from_map(k))
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class QueryInvoiceInfoByRequestNoResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        is_success: bool = None,
        return_value: QueryInvoiceInfoByRequestNoResponseBodyReturnValue = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.return_value = return_value

    def validate(self):
        if self.return_value:
            self.return_value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ReturnValue') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValue()
            self.return_value = temp_model.from_map(m['ReturnValue'])
        return self


class QueryInvoiceInfoByRequestNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryInvoiceInfoByRequestNoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMessageCallbackInfoRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.biz_type = biz_type
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryMessageCallbackInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryMessageCallbackInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMessageCallbackInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMessageCallbackInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMessageQueueListRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.biz_type = biz_type
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryMessageQueueListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryMessageQueueListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMessageQueueListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMessageQueueListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthlyBillInfoRequest(TeaModel):
    def __init__(
        self,
        bill_cycle: str = None,
        item_id: str = None,
        item_name: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject_item_id: str = None,
    ):
        self.bill_cycle = bill_cycle
        self.item_id = item_id
        self.item_name = item_name
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subject_item_id = subject_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subject_item_id is not None:
            result['SubjectItemId'] = self.subject_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SubjectItemId') is not None:
            self.subject_item_id = m.get('SubjectItemId')
        return self


class QueryMonthlyBillInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryMonthlyBillInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMonthlyBillInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMonthlyBillInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthlyStatisticsInfoRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        end_date: str = None,
        owner_id: int = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_date: str = None,
    ):
        self.bill_id = bill_id
        self.end_date = end_date
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class QueryMonthlyStatisticsInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryMonthlyStatisticsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMonthlyStatisticsInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMonthlyStatisticsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryNoBuyTasksRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryNoBuyTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryNoBuyTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryNoBuyTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryNoBuyTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryNoDistributeRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryNoDistributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryNoDistributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryNoDistributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryNoDistributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOpenStatusRequest(TeaModel):
    def __init__(
        self,
        bus_offer: int = None,
        owner_id: int = None,
        prod_code: str = None,
        prod_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bus_offer = bus_offer
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.prod_id = prod_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bus_offer is not None:
            result['BusOffer'] = self.bus_offer
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.prod_id is not None:
            result['ProdId'] = self.prod_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusOffer') is not None:
            self.bus_offer = m.get('BusOffer')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ProdId') is not None:
            self.prod_id = m.get('ProdId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryOpenStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryOpenStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOpenStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPackageDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryPackageDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPackageDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPackageDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPackageDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPackageListRequest(TeaModel):
    def __init__(
        self,
        bill_cycle: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_cycle = bill_cycle
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPackageListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPackageListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPackageListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPackageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPackageStatisticsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPackageStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPackageStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPackageStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPackageStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPoolCityListRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPoolCityListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPoolCityListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPoolCityListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPoolCityListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPoolInfoListRequest(TeaModel):
    def __init__(
        self,
        is_fuzzy_query: bool = None,
        owner_id: int = None,
        page_no: str = None,
        page_size: str = None,
        pool_name: str = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        search_param: str = None,
    ):
        self.is_fuzzy_query = is_fuzzy_query
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.pool_name = pool_name
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.search_param = search_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_fuzzy_query is not None:
            result['IsFuzzyQuery'] = self.is_fuzzy_query
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.search_param is not None:
            result['SearchParam'] = self.search_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsFuzzyQuery') is not None:
            self.is_fuzzy_query = m.get('IsFuzzyQuery')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SearchParam') is not None:
            self.search_param = m.get('SearchParam')
        return self


class QueryPoolInfoListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPoolInfoListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPoolInfoListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPoolInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPoolMonthlyBillInfoRequest(TeaModel):
    def __init__(
        self,
        bill_cycle: str = None,
        bill_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_cycle = bill_cycle
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPoolMonthlyBillInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPoolMonthlyBillInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPoolMonthlyBillInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPoolMonthlyBillInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPoolStatisticsInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPoolStatisticsInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPoolStatisticsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPoolStatisticsInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPoolStatisticsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPoolSummaryInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPoolSummaryInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPoolSummaryInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPoolSummaryInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPoolSummaryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPurchasedInfoRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPurchasedInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPurchasedInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPurchasedInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPurchasedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPurchasedResListRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        city: str = None,
        is_display_pool: bool = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        prod_code: str = None,
        res_bind_status: int = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.bill_id = bill_id
        self.city = city
        self.is_display_pool = is_display_pool
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.prod_code = prod_code
        self.res_bind_status = res_bind_status
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.city is not None:
            result['City'] = self.city
        if self.is_display_pool is not None:
            result['IsDisplayPool'] = self.is_display_pool
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_bind_status is not None:
            result['ResBindStatus'] = self.res_bind_status
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('IsDisplayPool') is not None:
            self.is_display_pool = m.get('IsDisplayPool')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResBindStatus') is not None:
            self.res_bind_status = m.get('ResBindStatus')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class QueryPurchasedResListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPurchasedResListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPurchasedResListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPurchasedResListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryQRCodeInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_number: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_number = secret_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_number is not None:
            result['SecretNumber'] = self.secret_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNumber') is not None:
            self.secret_number = m.get('SecretNumber')
        return self


class QueryQRCodeInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        token: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class QueryQRCodeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryQRCodeInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryQRCodeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordingUrlRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        call_date: str = None,
        call_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.call_date = call_date
        self.call_id = call_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.call_date is not None:
            result['CallDate'] = self.call_date
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('CallDate') is not None:
            self.call_date = m.get('CallDate')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRecordingUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryRecordingUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordingUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRecordingUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryResSummaryInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryResSummaryInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryResSummaryInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryResSummaryInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryResSummaryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRingToneUrlRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        file_key: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.file_key = file_key
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRingToneUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryRingToneUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRingToneUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRingToneUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRingTonesRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        play_type: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.play_type = play_type
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.play_type is not None:
            result['PlayType'] = self.play_type
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlayType') is not None:
            self.play_type = m.get('PlayType')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRingTonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryRingTonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRingTonesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRingTonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySimplePoolInfoListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        pool_name: str = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.pool_name = pool_name
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QuerySimplePoolInfoListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QuerySimplePoolInfoListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySimplePoolInfoListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySimplePoolInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStatisticsInfoRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        end_date: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_date: str = None,
    ):
        self.bill_id = bill_id
        self.end_date = end_date
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class QueryStatisticsInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryStatisticsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStatisticsInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryStatisticsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagOpenStatusRequest(TeaModel):
    def __init__(
        self,
        attribute_key: str = None,
        biz_type: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sub_attribute_key: str = None,
    ):
        self.attribute_key = attribute_key
        self.biz_type = biz_type
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sub_attribute_key = sub_attribute_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sub_attribute_key is not None:
            result['SubAttributeKey'] = self.sub_attribute_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SubAttributeKey') is not None:
            self.sub_attribute_key = m.get('SubAttributeKey')
        return self


class QueryTagOpenStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTagOpenStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTagOpenStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTagOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferDetailsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        prod_code: str = None,
        record_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.prod_code = prod_code
        self.record_id = record_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryTransferDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryTransferDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTransferDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTransferDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferRecordRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        record_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.record_id = record_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryTransferRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryTransferRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTransferRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTransferRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferRecordsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        prod_code: str = None,
        record_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.prod_code = prod_code
        self.record_id = record_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryTransferRecordsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryTransferRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTransferRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTransferRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserDeleteStatusRequest(TeaModel):
    def __init__(
        self,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        level: int = None,
        message: str = None,
        pk: str = None,
        prod_code: str = None,
        prompt: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
        url: str = None,
    ):
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.level = level
        self.message = message
        self.pk = pk
        self.prod_code = prod_code
        self.prompt = prompt
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryUserDeleteStatusResponseBody(TeaModel):
    def __init__(
        self,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        level: int = None,
        message: str = None,
        pk: str = None,
        prompt: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
        url: str = None,
    ):
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.level = level
        self.message = message
        self.pk = pk
        self.prompt = prompt
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryUserDeleteStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserDeleteStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryUserDeleteStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserResPoolInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryUserResPoolInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryUserResPoolInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserResPoolInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryUserResPoolInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVirtualOperationShowRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryVirtualOperationShowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryVirtualOperationShowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryVirtualOperationShowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryVirtualOperationShowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWarningListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryWarningListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryWarningListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWarningListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryWarningListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWaybillOrderInfoRequest(TeaModel):
    def __init__(
        self,
        outer_order_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.outer_order_code = outer_order_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryWaybillOrderInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        aliyunprice: str = None,
        appoint_got_end_time: str = None,
        appoint_got_start_time: str = None,
        biz_type: int = None,
        city: str = None,
        cp_code: str = None,
        got_code: str = None,
        last_logistic_detail: str = None,
        logistics_gmt_modified: str = None,
        logistics_status: str = None,
        logistics_status_desc: str = None,
        mail_no: str = None,
        outer_order_code: str = None,
    ):
        self.aliyunprice = aliyunprice
        self.appoint_got_end_time = appoint_got_end_time
        self.appoint_got_start_time = appoint_got_start_time
        self.biz_type = biz_type
        self.city = city
        self.cp_code = cp_code
        self.got_code = got_code
        self.last_logistic_detail = last_logistic_detail
        self.logistics_gmt_modified = logistics_gmt_modified
        self.logistics_status = logistics_status
        self.logistics_status_desc = logistics_status_desc
        self.mail_no = mail_no
        self.outer_order_code = outer_order_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyunprice is not None:
            result['Aliyunprice'] = self.aliyunprice
        if self.appoint_got_end_time is not None:
            result['AppointGotEndTime'] = self.appoint_got_end_time
        if self.appoint_got_start_time is not None:
            result['AppointGotStartTime'] = self.appoint_got_start_time
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.city is not None:
            result['City'] = self.city
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.got_code is not None:
            result['GotCode'] = self.got_code
        if self.last_logistic_detail is not None:
            result['LastLogisticDetail'] = self.last_logistic_detail
        if self.logistics_gmt_modified is not None:
            result['LogisticsGmtModified'] = self.logistics_gmt_modified
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.logistics_status_desc is not None:
            result['LogisticsStatusDesc'] = self.logistics_status_desc
        if self.mail_no is not None:
            result['MailNo'] = self.mail_no
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliyunprice') is not None:
            self.aliyunprice = m.get('Aliyunprice')
        if m.get('AppointGotEndTime') is not None:
            self.appoint_got_end_time = m.get('AppointGotEndTime')
        if m.get('AppointGotStartTime') is not None:
            self.appoint_got_start_time = m.get('AppointGotStartTime')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('GotCode') is not None:
            self.got_code = m.get('GotCode')
        if m.get('LastLogisticDetail') is not None:
            self.last_logistic_detail = m.get('LastLogisticDetail')
        if m.get('LogisticsGmtModified') is not None:
            self.logistics_gmt_modified = m.get('LogisticsGmtModified')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('LogisticsStatusDesc') is not None:
            self.logistics_status_desc = m.get('LogisticsStatusDesc')
        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        return self


class QueryWaybillOrderInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryWaybillOrderInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryWaybillOrderInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryWaybillOrderInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWaybillOrderInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryWaybillOrderInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWaybillOrderStatisticsInfoRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        granularity: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.granularity = granularity
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryWaybillOrderStatisticsInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        aliyunprice_amount: float = None,
        cancel_count: int = None,
        gmt_create: str = None,
        got_count: int = None,
        order_total: int = None,
    ):
        self.aliyunprice_amount = aliyunprice_amount
        self.cancel_count = cancel_count
        self.gmt_create = gmt_create
        self.got_count = got_count
        self.order_total = order_total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyunprice_amount is not None:
            result['AliyunpriceAmount'] = self.aliyunprice_amount
        if self.cancel_count is not None:
            result['CancelCount'] = self.cancel_count
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.got_count is not None:
            result['GotCount'] = self.got_count
        if self.order_total is not None:
            result['OrderTotal'] = self.order_total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunpriceAmount') is not None:
            self.aliyunprice_amount = m.get('AliyunpriceAmount')
        if m.get('CancelCount') is not None:
            self.cancel_count = m.get('CancelCount')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GotCount') is not None:
            self.got_count = m.get('GotCount')
        if m.get('OrderTotal') is not None:
            self.order_total = m.get('OrderTotal')
        return self


class QueryWaybillOrderStatisticsInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryWaybillOrderStatisticsInfoResponseBodyData] = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryWaybillOrderStatisticsInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWaybillOrderStatisticsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWaybillOrderStatisticsInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryWaybillOrderStatisticsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseResourceRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        is_display_pool: bool = None,
        owner_id: int = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.bill_id = bill_id
        self.is_display_pool = is_display_pool
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.is_display_pool is not None:
            result['IsDisplayPool'] = self.is_display_pool
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('IsDisplayPool') is not None:
            self.is_display_pool = m.get('IsDisplayPool')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class ReleaseResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ReleaseResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestTtsRingToneRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tts: str = None,
        voice_speed: str = None,
        voice_style: str = None,
        voice_type: str = None,
        voice_volume: str = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tts = tts
        self.voice_speed = voice_speed
        self.voice_style = voice_style
        self.voice_type = voice_type
        self.voice_volume = voice_volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tts is not None:
            result['Tts'] = self.tts
        if self.voice_speed is not None:
            result['VoiceSpeed'] = self.voice_speed
        if self.voice_style is not None:
            result['VoiceStyle'] = self.voice_style
        if self.voice_type is not None:
            result['VoiceType'] = self.voice_type
        if self.voice_volume is not None:
            result['VoiceVolume'] = self.voice_volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tts') is not None:
            self.tts = m.get('Tts')
        if m.get('VoiceSpeed') is not None:
            self.voice_speed = m.get('VoiceSpeed')
        if m.get('VoiceStyle') is not None:
            self.voice_style = m.get('VoiceStyle')
        if m.get('VoiceType') is not None:
            self.voice_type = m.get('VoiceType')
        if m.get('VoiceVolume') is not None:
            self.voice_volume = m.get('VoiceVolume')
        return self


class TestTtsRingToneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class TestTtsRingToneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TestTtsRingToneResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TestTtsRingToneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindResourceRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        bind_ids: str = None,
        owner_id: int = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.bill_id = bill_id
        self.bind_ids = bind_ids
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.bind_ids is not None:
            result['BindIds'] = self.bind_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BindIds') is not None:
            self.bind_ids = m.get('BindIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class UnbindResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UnbindResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockResourceRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class UnlockResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UnlockResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnlockResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnlockResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateContactsRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        id: int = None,
        name: str = None,
        owner_id: int = None,
        phone_number: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.phone_number = phone_number
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateContactsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdateContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateContactsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupDetailRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        id: str = None,
        owner_id: int = None,
        pool_key: str = None,
        prod_code: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.group_id = group_id
        self.id = id
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.prod_code = prod_code
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdateGroupDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGroupDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupInfoRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        owner_id: int = None,
        pool_key: str = None,
        prod_code: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.prod_code = prod_code
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateGroupInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdateGroupInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGroupInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGroupInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePoolNameRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        pool_name: str = None,
        prod_code: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.pool_name = pool_name
        self.prod_code = prod_code
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdatePoolNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdatePoolNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePoolNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePoolNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResRemarkRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        owner_id: int = None,
        prod_code: str = None,
        remark: str = None,
        res_type: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.bill_id = bill_id
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.remark = remark
        self.res_type = res_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class UpdateResRemarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdateResRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResRemarkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateOrderRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        data: str = None,
    ):
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ValidateOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


