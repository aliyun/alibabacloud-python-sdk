# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class QueryInstanceResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QueryInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        contact_mail: str = None,
        country_id: str = None,
        cust_type: str = None,
        facebook_bm_id: str = None,
        instance_description: str = None,
        instance_id: str = None,
        instance_name: str = None,
        isv_terms: str = None,
        office_address: str = None,
        resource_group_id: str = None,
        resource_region_id: str = None,
        submit_time: str = None,
    ):
        self.channel_type = channel_type
        self.contact_mail = contact_mail
        self.country_id = country_id
        self.cust_type = cust_type
        # FacebookBmId
        self.facebook_bm_id = facebook_bm_id
        self.instance_description = instance_description
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.isv_terms = isv_terms
        self.office_address = office_address
        self.resource_group_id = resource_group_id
        self.resource_region_id = resource_region_id
        self.submit_time = submit_time

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

        if self.cust_type is not None:
            result['CustType'] = self.cust_type

        if self.facebook_bm_id is not None:
            result['FacebookBmId'] = self.facebook_bm_id

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.isv_terms is not None:
            result['IsvTerms'] = self.isv_terms

        if self.office_address is not None:
            result['OfficeAddress'] = self.office_address

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('ContactMail') is not None:
            self.contact_mail = m.get('ContactMail')

        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')

        if m.get('CustType') is not None:
            self.cust_type = m.get('CustType')

        if m.get('FacebookBmId') is not None:
            self.facebook_bm_id = m.get('FacebookBmId')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsvTerms') is not None:
            self.isv_terms = m.get('IsvTerms')

        if m.get('OfficeAddress') is not None:
            self.office_address = m.get('OfficeAddress')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        return self

