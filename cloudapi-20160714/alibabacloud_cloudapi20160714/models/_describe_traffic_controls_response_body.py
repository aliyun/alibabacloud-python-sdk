# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeTrafficControlsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        traffic_controls: main_models.DescribeTrafficControlsResponseBodyTrafficControls = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count
        # The returned throttling policy information. It is an array consisting of TrafficControl data.
        self.traffic_controls = traffic_controls

    def validate(self):
        if self.traffic_controls:
            self.traffic_controls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.traffic_controls is not None:
            result['TrafficControls'] = self.traffic_controls.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TrafficControls') is not None:
            temp_model = main_models.DescribeTrafficControlsResponseBodyTrafficControls()
            self.traffic_controls = temp_model.from_map(m.get('TrafficControls'))

        return self

class DescribeTrafficControlsResponseBodyTrafficControls(DaraModel):
    def __init__(
        self,
        traffic_control: List[main_models.DescribeTrafficControlsResponseBodyTrafficControlsTrafficControl] = None,
    ):
        self.traffic_control = traffic_control

    def validate(self):
        if self.traffic_control:
            for v1 in self.traffic_control:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TrafficControl'] = []
        if self.traffic_control is not None:
            for k1 in self.traffic_control:
                result['TrafficControl'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_control = []
        if m.get('TrafficControl') is not None:
            for k1 in m.get('TrafficControl'):
                temp_model = main_models.DescribeTrafficControlsResponseBodyTrafficControlsTrafficControl()
                self.traffic_control.append(temp_model.from_map(k1))

        return self

class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControl(DaraModel):
    def __init__(
        self,
        api_default: int = None,
        app_default: int = None,
        created_time: str = None,
        description: str = None,
        modified_time: str = None,
        special_policies: main_models.DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPolicies = None,
        traffic_control_id: str = None,
        traffic_control_name: str = None,
        traffic_control_unit: str = None,
        user_default: int = None,
    ):
        # The default throttling value for each API.
        self.api_default = api_default
        # The default throttling value for each app.
        self.app_default = app_default
        # The creation time (UTC) of the throttling policy.
        self.created_time = created_time
        # The description of the throttling policy.
        self.description = description
        # The last modification time (UTC) of the throttling policy.
        self.modified_time = modified_time
        # The returned information about a special throttling policy. It is an array consisting of SpecialPolicy data.
        self.special_policies = special_policies
        # The ID of the throttling policy.
        self.traffic_control_id = traffic_control_id
        # The name of the throttling policy.
        self.traffic_control_name = traffic_control_name
        # The unit to be used in the throttling policy. Valid values:
        # 
        # *   MINUTE
        # *   HOUR
        # *   DAY
        self.traffic_control_unit = traffic_control_unit
        # The default throttling value for each user.
        self.user_default = user_default

    def validate(self):
        if self.special_policies:
            self.special_policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_default is not None:
            result['ApiDefault'] = self.api_default

        if self.app_default is not None:
            result['AppDefault'] = self.app_default

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.special_policies is not None:
            result['SpecialPolicies'] = self.special_policies.to_map()

        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id

        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name

        if self.traffic_control_unit is not None:
            result['TrafficControlUnit'] = self.traffic_control_unit

        if self.user_default is not None:
            result['UserDefault'] = self.user_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDefault') is not None:
            self.api_default = m.get('ApiDefault')

        if m.get('AppDefault') is not None:
            self.app_default = m.get('AppDefault')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('SpecialPolicies') is not None:
            temp_model = main_models.DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPolicies()
            self.special_policies = temp_model.from_map(m.get('SpecialPolicies'))

        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')

        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')

        if m.get('TrafficControlUnit') is not None:
            self.traffic_control_unit = m.get('TrafficControlUnit')

        if m.get('UserDefault') is not None:
            self.user_default = m.get('UserDefault')

        return self

class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPolicies(DaraModel):
    def __init__(
        self,
        special_policy: List[main_models.DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicy] = None,
    ):
        self.special_policy = special_policy

    def validate(self):
        if self.special_policy:
            for v1 in self.special_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SpecialPolicy'] = []
        if self.special_policy is not None:
            for k1 in self.special_policy:
                result['SpecialPolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.special_policy = []
        if m.get('SpecialPolicy') is not None:
            for k1 in m.get('SpecialPolicy'):
                temp_model = main_models.DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicy()
                self.special_policy.append(temp_model.from_map(k1))

        return self

class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicy(DaraModel):
    def __init__(
        self,
        special_type: str = None,
        specials: main_models.DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecials = None,
    ):
        # The type of the special throttling policy. Valid values:
        # 
        # *   **APP**
        # *   **USER**
        self.special_type = special_type
        # The returned information about a special throttling policy. It is an array consisting of Special data.
        self.specials = specials

    def validate(self):
        if self.specials:
            self.specials.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.special_type is not None:
            result['SpecialType'] = self.special_type

        if self.specials is not None:
            result['Specials'] = self.specials.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecialType') is not None:
            self.special_type = m.get('SpecialType')

        if m.get('Specials') is not None:
            temp_model = main_models.DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecials()
            self.specials = temp_model.from_map(m.get('Specials'))

        return self

class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecials(DaraModel):
    def __init__(
        self,
        special: List[main_models.DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecialsSpecial] = None,
    ):
        self.special = special

    def validate(self):
        if self.special:
            for v1 in self.special:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Special'] = []
        if self.special is not None:
            for k1 in self.special:
                result['Special'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.special = []
        if m.get('Special') is not None:
            for k1 in m.get('Special'):
                temp_model = main_models.DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecialsSpecial()
                self.special.append(temp_model.from_map(k1))

        return self

class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecialsSpecial(DaraModel):
    def __init__(
        self,
        special_key: str = None,
        traffic_value: int = None,
    ):
        # The AppId or user account corresponding to SpecialType.
        self.special_key = special_key
        # The throttling value.
        self.traffic_value = traffic_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.special_key is not None:
            result['SpecialKey'] = self.special_key

        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecialKey') is not None:
            self.special_key = m.get('SpecialKey')

        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')

        return self

