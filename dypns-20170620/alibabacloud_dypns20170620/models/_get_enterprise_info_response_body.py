# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dypns20170620 import models as main_models
from darabonba.model import DaraModel

class GetEnterpriseInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetEnterpriseInfoResponseBodyData = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.GetEnterpriseInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetEnterpriseInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        audit_desc: str = None,
        audit_time: str = None,
        business_license_address: str = None,
        business_license_picture: str = None,
        enterprise_id: int = None,
        enterprise_name: str = None,
        legal_person_cert_number: str = None,
        legal_person_cert_picture: str = None,
        legal_person_name: str = None,
        manager_cert_number: str = None,
        manager_cert_picture: str = None,
        manager_contact_number: str = None,
        manager_name: str = None,
        number_application_letter_picture: str = None,
        order_id: int = None,
        organization_code: str = None,
        remark: str = None,
        status: int = None,
        undertaking_picture: str = None,
    ):
        self.audit_desc = audit_desc
        self.audit_time = audit_time
        self.business_license_address = business_license_address
        self.business_license_picture = business_license_picture
        self.enterprise_id = enterprise_id
        self.enterprise_name = enterprise_name
        self.legal_person_cert_number = legal_person_cert_number
        self.legal_person_cert_picture = legal_person_cert_picture
        self.legal_person_name = legal_person_name
        self.manager_cert_number = manager_cert_number
        self.manager_cert_picture = manager_cert_picture
        self.manager_contact_number = manager_contact_number
        self.manager_name = manager_name
        self.number_application_letter_picture = number_application_letter_picture
        self.order_id = order_id
        self.organization_code = organization_code
        self.remark = remark
        self.status = status
        self.undertaking_picture = undertaking_picture

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_desc is not None:
            result['AuditDesc'] = self.audit_desc

        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time

        if self.business_license_address is not None:
            result['BusinessLicenseAddress'] = self.business_license_address

        if self.business_license_picture is not None:
            result['BusinessLicensePicture'] = self.business_license_picture

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.enterprise_name is not None:
            result['EnterpriseName'] = self.enterprise_name

        if self.legal_person_cert_number is not None:
            result['LegalPersonCertNumber'] = self.legal_person_cert_number

        if self.legal_person_cert_picture is not None:
            result['LegalPersonCertPicture'] = self.legal_person_cert_picture

        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name

        if self.manager_cert_number is not None:
            result['ManagerCertNumber'] = self.manager_cert_number

        if self.manager_cert_picture is not None:
            result['ManagerCertPicture'] = self.manager_cert_picture

        if self.manager_contact_number is not None:
            result['ManagerContactNumber'] = self.manager_contact_number

        if self.manager_name is not None:
            result['ManagerName'] = self.manager_name

        if self.number_application_letter_picture is not None:
            result['NumberApplicationLetterPicture'] = self.number_application_letter_picture

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.undertaking_picture is not None:
            result['UndertakingPicture'] = self.undertaking_picture

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditDesc') is not None:
            self.audit_desc = m.get('AuditDesc')

        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')

        if m.get('BusinessLicenseAddress') is not None:
            self.business_license_address = m.get('BusinessLicenseAddress')

        if m.get('BusinessLicensePicture') is not None:
            self.business_license_picture = m.get('BusinessLicensePicture')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('EnterpriseName') is not None:
            self.enterprise_name = m.get('EnterpriseName')

        if m.get('LegalPersonCertNumber') is not None:
            self.legal_person_cert_number = m.get('LegalPersonCertNumber')

        if m.get('LegalPersonCertPicture') is not None:
            self.legal_person_cert_picture = m.get('LegalPersonCertPicture')

        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')

        if m.get('ManagerCertNumber') is not None:
            self.manager_cert_number = m.get('ManagerCertNumber')

        if m.get('ManagerCertPicture') is not None:
            self.manager_cert_picture = m.get('ManagerCertPicture')

        if m.get('ManagerContactNumber') is not None:
            self.manager_contact_number = m.get('ManagerContactNumber')

        if m.get('ManagerName') is not None:
            self.manager_name = m.get('ManagerName')

        if m.get('NumberApplicationLetterPicture') is not None:
            self.number_application_letter_picture = m.get('NumberApplicationLetterPicture')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UndertakingPicture') is not None:
            self.undertaking_picture = m.get('UndertakingPicture')

        return self

