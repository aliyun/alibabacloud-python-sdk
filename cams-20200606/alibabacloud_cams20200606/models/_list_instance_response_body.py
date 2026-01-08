# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListInstanceResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.ListInstanceResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        contact_mail: str = None,
        country_id: str = None,
        cust_space_id: str = None,
        facebook_bm_id: str = None,
        instance_description: str = None,
        instance_id: str = None,
        instance_name: str = None,
        isv_terms: str = None,
        office_address: str = None,
        resource_group_id: str = None,
        resource_region_id: str = None,
        state: str = None,
        submit_time: str = None,
    ):
        self.channel_type = channel_type
        self.contact_mail = contact_mail
        self.country_id = country_id
        self.cust_space_id = cust_space_id
        self.facebook_bm_id = facebook_bm_id
        self.instance_description = instance_description
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.isv_terms = isv_terms
        self.office_address = office_address
        self.resource_group_id = resource_group_id
        self.resource_region_id = resource_region_id
        self.state = state
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

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

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

        if self.state is not None:
            result['State'] = self.state

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

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

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

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        return self

