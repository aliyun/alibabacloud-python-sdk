# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        contact_mail: str = None,
        country_id: str = None,
        facebook_bm_id: str = None,
        instance_description: str = None,
        instance_name: str = None,
        is_confirm_audit: str = None,
        isv_terms: str = None,
        office_address: str = None,
        resource_group_id: str = None,
    ):
        # The channel type.
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # The contact email address.
        self.contact_mail = contact_mail
        # The country code.
        self.country_id = country_id
        # The ID of the Facebook Business Manager (BM).
        self.facebook_bm_id = facebook_bm_id
        # The description of the instance.
        self.instance_description = instance_description
        # The name of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # Specifies whether to confirm the audit.
        self.is_confirm_audit = is_confirm_audit
        # The URL of the ISV terms file.
        self.isv_terms = isv_terms
        # The office address of the business.
        self.office_address = office_address
        # The ID of the resource group that contains the instance.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.contact_mail is not None:
            result['ContactMail'] = self.contact_mail

        if self.country_id is not None:
            result['CountryId'] = self.country_id

        if self.facebook_bm_id is not None:
            result['FacebookBmId'] = self.facebook_bm_id

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_confirm_audit is not None:
            result['IsConfirmAudit'] = self.is_confirm_audit

        if self.isv_terms is not None:
            result['IsvTerms'] = self.isv_terms

        if self.office_address is not None:
            result['OfficeAddress'] = self.office_address

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('ContactMail') is not None:
            self.contact_mail = m.get('ContactMail')

        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')

        if m.get('FacebookBmId') is not None:
            self.facebook_bm_id = m.get('FacebookBmId')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsConfirmAudit') is not None:
            self.is_confirm_audit = m.get('IsConfirmAudit')

        if m.get('IsvTerms') is not None:
            self.isv_terms = m.get('IsvTerms')

        if m.get('OfficeAddress') is not None:
            self.office_address = m.get('OfficeAddress')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

