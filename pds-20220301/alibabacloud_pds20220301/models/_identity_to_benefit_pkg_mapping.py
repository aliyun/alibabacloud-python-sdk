# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class IdentityToBenefitPkgMapping(DaraModel):
    def __init__(
        self,
        benefit_pkg_computation_rule: str = None,
        benefit_pkg_id: str = None,
        benefit_pkg_name: str = None,
        benefit_pkg_owner_id: str = None,
        benefit_pkg_priority: int = None,
        benefit_pkg_type: str = None,
        created_at: str = None,
        delivery_info_list: List[main_models.BenefitPkgDeliveryInfo] = None,
        identity_id: str = None,
        identity_type: str = None,
        updated_at: str = None,
    ):
        # Calculation rules of equity in the benefit package.
        # 
        # The user identity benefit package. The return value is empty. Only the quota of the effective equity is calculated based on the priority.
        # 
        # The user resource benefit package, which can return null or non-null values. If the return value is not empty, this benefit package is used to append the quota of existing benefits in other benefit packages, which is limited to quota-type benefits. For example, if a user identity benefit package already contains 10 GB of user storage capacity, you can define one or more user resource benefit packages to add additional storage capacity for some users.
        # 
        # The following append calculation rules are supported:
        # 
        # sum: Multiple benefit packages have the same equity and are accumulated.
        # 
        # max: If multiple benefit packages have the same equity, the max value is used.
        # 
        # min: If multiple benefit packages have the same equity, the value of min is used.
        self.benefit_pkg_computation_rule = benefit_pkg_computation_rule
        # The ID of the benefit package.
        self.benefit_pkg_id = benefit_pkg_id
        # The name of the benefit package.
        self.benefit_pkg_name = benefit_pkg_name
        # The ID of the owner of the benefit package.
        self.benefit_pkg_owner_id = benefit_pkg_owner_id
        # Priority of the benefit package.
        # 
        # The priority returned for the user identity benefit package. A smaller number indicates a higher priority.
        self.benefit_pkg_priority = benefit_pkg_priority
        # The type of benefit package.
        # 
        # Valid values:
        # 
        # user_identity : user identity benefit package
        # 
        # user_resource: user resource benefit package
        self.benefit_pkg_type = benefit_pkg_type
        # Creation time of the entity and benefit package association.
        self.created_at = created_at
        # The information about the benefit packages that are associated with an entity.
        self.delivery_info_list = delivery_info_list
        # The ID of the entity.
        self.identity_id = identity_id
        # The type of the entity.
        self.identity_type = identity_type
        # Update time associated with the entity and benefit package.
        self.updated_at = updated_at

    def validate(self):
        if self.delivery_info_list:
            for v1 in self.delivery_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.benefit_pkg_computation_rule is not None:
            result['benefit_pkg_computation_rule'] = self.benefit_pkg_computation_rule

        if self.benefit_pkg_id is not None:
            result['benefit_pkg_id'] = self.benefit_pkg_id

        if self.benefit_pkg_name is not None:
            result['benefit_pkg_name'] = self.benefit_pkg_name

        if self.benefit_pkg_owner_id is not None:
            result['benefit_pkg_owner_id'] = self.benefit_pkg_owner_id

        if self.benefit_pkg_priority is not None:
            result['benefit_pkg_priority'] = self.benefit_pkg_priority

        if self.benefit_pkg_type is not None:
            result['benefit_pkg_type'] = self.benefit_pkg_type

        if self.created_at is not None:
            result['created_at'] = self.created_at

        result['delivery_info_list'] = []
        if self.delivery_info_list is not None:
            for k1 in self.delivery_info_list:
                result['delivery_info_list'].append(k1.to_map() if k1 else None)

        if self.identity_id is not None:
            result['identity_id'] = self.identity_id

        if self.identity_type is not None:
            result['identity_type'] = self.identity_type

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('benefit_pkg_computation_rule') is not None:
            self.benefit_pkg_computation_rule = m.get('benefit_pkg_computation_rule')

        if m.get('benefit_pkg_id') is not None:
            self.benefit_pkg_id = m.get('benefit_pkg_id')

        if m.get('benefit_pkg_name') is not None:
            self.benefit_pkg_name = m.get('benefit_pkg_name')

        if m.get('benefit_pkg_owner_id') is not None:
            self.benefit_pkg_owner_id = m.get('benefit_pkg_owner_id')

        if m.get('benefit_pkg_priority') is not None:
            self.benefit_pkg_priority = m.get('benefit_pkg_priority')

        if m.get('benefit_pkg_type') is not None:
            self.benefit_pkg_type = m.get('benefit_pkg_type')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        self.delivery_info_list = []
        if m.get('delivery_info_list') is not None:
            for k1 in m.get('delivery_info_list'):
                temp_model = main_models.BenefitPkgDeliveryInfo()
                self.delivery_info_list.append(temp_model.from_map(k1))

        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')

        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

