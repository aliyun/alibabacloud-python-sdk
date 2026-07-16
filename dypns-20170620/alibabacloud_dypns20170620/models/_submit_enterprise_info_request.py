# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitEnterpriseInfoRequest(DaraModel):
    def __init__(
        self,
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
        organization_code: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        undertaking_picture: str = None,
    ):
        # This parameter is required.
        self.business_license_address = business_license_address
        # This parameter is required.
        self.business_license_picture = business_license_picture
        self.enterprise_id = enterprise_id
        # This parameter is required.
        self.enterprise_name = enterprise_name
        # This parameter is required.
        self.legal_person_cert_number = legal_person_cert_number
        # This parameter is required.
        self.legal_person_cert_picture = legal_person_cert_picture
        # This parameter is required.
        self.legal_person_name = legal_person_name
        # This parameter is required.
        self.manager_cert_number = manager_cert_number
        # This parameter is required.
        self.manager_cert_picture = manager_cert_picture
        # This parameter is required.
        self.manager_contact_number = manager_contact_number
        # This parameter is required.
        self.manager_name = manager_name
        # This parameter is required.
        self.number_application_letter_picture = number_application_letter_picture
        # This parameter is required.
        self.organization_code = organization_code
        self.owner_id = owner_id
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.undertaking_picture = undertaking_picture

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.undertaking_picture is not None:
            result['UndertakingPicture'] = self.undertaking_picture

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UndertakingPicture') is not None:
            self.undertaking_picture = m.get('UndertakingPicture')

        return self

