# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class FindCustomerSnapshotResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        customer_snapshot: main_models.FindCustomerSnapshotResponseBodyCustomerSnapshot = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.customer_snapshot = customer_snapshot
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.customer_snapshot:
            self.customer_snapshot.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.customer_snapshot is not None:
            result['CustomerSnapshot'] = self.customer_snapshot.to_map()

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

        if m.get('CustomerSnapshot') is not None:
            temp_model = main_models.FindCustomerSnapshotResponseBodyCustomerSnapshot()
            self.customer_snapshot = temp_model.from_map(m.get('CustomerSnapshot'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class FindCustomerSnapshotResponseBodyCustomerSnapshot(DaraModel):
    def __init__(
        self,
        account_info_snapshot_model: main_models.FindCustomerSnapshotResponseBodyCustomerSnapshotAccountInfoSnapshotModel = None,
        account_tax_snapshot_model: main_models.FindCustomerSnapshotResponseBodyCustomerSnapshotAccountTaxSnapshotModel = None,
        gmt_create: str = None,
        id: int = None,
        info_type: str = None,
        kp_id: int = None,
    ):
        self.account_info_snapshot_model = account_info_snapshot_model
        self.account_tax_snapshot_model = account_tax_snapshot_model
        self.gmt_create = gmt_create
        self.id = id
        self.info_type = info_type
        self.kp_id = kp_id

    def validate(self):
        if self.account_info_snapshot_model:
            self.account_info_snapshot_model.validate()
        if self.account_tax_snapshot_model:
            self.account_tax_snapshot_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_info_snapshot_model is not None:
            result['AccountInfoSnapshotModel'] = self.account_info_snapshot_model.to_map()

        if self.account_tax_snapshot_model is not None:
            result['AccountTaxSnapshotModel'] = self.account_tax_snapshot_model.to_map()

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.info_type is not None:
            result['InfoType'] = self.info_type

        if self.kp_id is not None:
            result['KpId'] = self.kp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountInfoSnapshotModel') is not None:
            temp_model = main_models.FindCustomerSnapshotResponseBodyCustomerSnapshotAccountInfoSnapshotModel()
            self.account_info_snapshot_model = temp_model.from_map(m.get('AccountInfoSnapshotModel'))

        if m.get('AccountTaxSnapshotModel') is not None:
            temp_model = main_models.FindCustomerSnapshotResponseBodyCustomerSnapshotAccountTaxSnapshotModel()
            self.account_tax_snapshot_model = temp_model.from_map(m.get('AccountTaxSnapshotModel'))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')

        if m.get('KpId') is not None:
            self.kp_id = m.get('KpId')

        return self

class FindCustomerSnapshotResponseBodyCustomerSnapshotAccountTaxSnapshotModel(DaraModel):
    def __init__(
        self,
        finance_tax_certificate_img_name: str = None,
        finance_tax_certificate_img_url: str = None,
        second_finance_tax: str = None,
        second_finance_tax_certificate_img_name: str = None,
        second_finance_tax_certificate_img_url: str = None,
        tax: str = None,
    ):
        self.finance_tax_certificate_img_name = finance_tax_certificate_img_name
        self.finance_tax_certificate_img_url = finance_tax_certificate_img_url
        self.second_finance_tax = second_finance_tax
        self.second_finance_tax_certificate_img_name = second_finance_tax_certificate_img_name
        self.second_finance_tax_certificate_img_url = second_finance_tax_certificate_img_url
        self.tax = tax

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finance_tax_certificate_img_name is not None:
            result['FinanceTaxCertificateImgName'] = self.finance_tax_certificate_img_name

        if self.finance_tax_certificate_img_url is not None:
            result['FinanceTaxCertificateImgUrl'] = self.finance_tax_certificate_img_url

        if self.second_finance_tax is not None:
            result['SecondFinanceTax'] = self.second_finance_tax

        if self.second_finance_tax_certificate_img_name is not None:
            result['SecondFinanceTaxCertificateImgName'] = self.second_finance_tax_certificate_img_name

        if self.second_finance_tax_certificate_img_url is not None:
            result['SecondFinanceTaxCertificateImgUrl'] = self.second_finance_tax_certificate_img_url

        if self.tax is not None:
            result['Tax'] = self.tax

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinanceTaxCertificateImgName') is not None:
            self.finance_tax_certificate_img_name = m.get('FinanceTaxCertificateImgName')

        if m.get('FinanceTaxCertificateImgUrl') is not None:
            self.finance_tax_certificate_img_url = m.get('FinanceTaxCertificateImgUrl')

        if m.get('SecondFinanceTax') is not None:
            self.second_finance_tax = m.get('SecondFinanceTax')

        if m.get('SecondFinanceTaxCertificateImgName') is not None:
            self.second_finance_tax_certificate_img_name = m.get('SecondFinanceTaxCertificateImgName')

        if m.get('SecondFinanceTaxCertificateImgUrl') is not None:
            self.second_finance_tax_certificate_img_url = m.get('SecondFinanceTaxCertificateImgUrl')

        if m.get('Tax') is not None:
            self.tax = m.get('Tax')

        return self

class FindCustomerSnapshotResponseBodyCustomerSnapshotAccountInfoSnapshotModel(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_2: str = None,
        address_3: str = None,
        address_4: str = None,
        address_5: str = None,
        address_6: str = None,
        city_id: str = None,
        city_name: str = None,
        post_code: str = None,
        province_id: str = None,
        province_name: str = None,
        true_name: str = None,
    ):
        self.address = address
        self.address_2 = address_2
        self.address_3 = address_3
        self.address_4 = address_4
        self.address_5 = address_5
        self.address_6 = address_6
        self.city_id = city_id
        self.city_name = city_name
        self.post_code = post_code
        self.province_id = province_id
        self.province_name = province_name
        self.true_name = true_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_2 is not None:
            result['Address2'] = self.address_2

        if self.address_3 is not None:
            result['Address3'] = self.address_3

        if self.address_4 is not None:
            result['Address4'] = self.address_4

        if self.address_5 is not None:
            result['Address5'] = self.address_5

        if self.address_6 is not None:
            result['Address6'] = self.address_6

        if self.city_id is not None:
            result['CityId'] = self.city_id

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.post_code is not None:
            result['PostCode'] = self.post_code

        if self.province_id is not None:
            result['ProvinceId'] = self.province_id

        if self.province_name is not None:
            result['ProvinceName'] = self.province_name

        if self.true_name is not None:
            result['TrueName'] = self.true_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Address2') is not None:
            self.address_2 = m.get('Address2')

        if m.get('Address3') is not None:
            self.address_3 = m.get('Address3')

        if m.get('Address4') is not None:
            self.address_4 = m.get('Address4')

        if m.get('Address5') is not None:
            self.address_5 = m.get('Address5')

        if m.get('Address6') is not None:
            self.address_6 = m.get('Address6')

        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')

        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')

        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')

        if m.get('TrueName') is not None:
            self.true_name = m.get('TrueName')

        return self

