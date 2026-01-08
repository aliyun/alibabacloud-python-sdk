# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChatappTemplateMetricRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        end: int = None,
        granularity: str = None,
        isv_code: str = None,
        language: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start: int = None,
        template_code: str = None,
        template_type: str = None,
    ):
        # The space ID of the RAM user within the ISV account.
        self.cust_space_id = cust_space_id
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end = end
        # The granularity of the metric.
        # 
        # Valid values:
        # 
        # *   DAILY
        # *   HALF_HOUR
        self.granularity = granularity
        # The independent software vendor (ISV) verification code, which is used to verify whether the RAM user is authorized by the ISV account.
        self.isv_code = isv_code
        # The template language.
        self.language = language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start = start
        # The template code.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The template type. If you do not specify this parameter, the default value WHATSAPP is used.
        # 
        # Valid values:
        # 
        # *   VIBER
        # *   WHATSAPP
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.end is not None:
            result['End'] = self.end

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code

        if self.language is not None:
            result['Language'] = self.language

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start is not None:
            result['Start'] = self.start

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

