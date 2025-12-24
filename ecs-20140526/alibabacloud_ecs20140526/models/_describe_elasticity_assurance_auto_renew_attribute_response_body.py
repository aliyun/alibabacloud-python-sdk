# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticityAssuranceAutoRenewAttributeResponseBody(DaraModel):
    def __init__(
        self,
        elasticity_assurance_renew_attributes: main_models.DescribeElasticityAssuranceAutoRenewAttributeResponseBodyElasticityAssuranceRenewAttributes = None,
        request_id: str = None,
    ):
        # The auto-renewal attribute of the elasticity assurances.
        self.elasticity_assurance_renew_attributes = elasticity_assurance_renew_attributes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.elasticity_assurance_renew_attributes:
            self.elasticity_assurance_renew_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elasticity_assurance_renew_attributes is not None:
            result['ElasticityAssuranceRenewAttributes'] = self.elasticity_assurance_renew_attributes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticityAssuranceRenewAttributes') is not None:
            temp_model = main_models.DescribeElasticityAssuranceAutoRenewAttributeResponseBodyElasticityAssuranceRenewAttributes()
            self.elasticity_assurance_renew_attributes = temp_model.from_map(m.get('ElasticityAssuranceRenewAttributes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeElasticityAssuranceAutoRenewAttributeResponseBodyElasticityAssuranceRenewAttributes(DaraModel):
    def __init__(
        self,
        elasticity_assurance_renew_attribute: List[main_models.DescribeElasticityAssuranceAutoRenewAttributeResponseBodyElasticityAssuranceRenewAttributesElasticityAssuranceRenewAttribute] = None,
    ):
        self.elasticity_assurance_renew_attribute = elasticity_assurance_renew_attribute

    def validate(self):
        if self.elasticity_assurance_renew_attribute:
            for v1 in self.elasticity_assurance_renew_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ElasticityAssuranceRenewAttribute'] = []
        if self.elasticity_assurance_renew_attribute is not None:
            for k1 in self.elasticity_assurance_renew_attribute:
                result['ElasticityAssuranceRenewAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elasticity_assurance_renew_attribute = []
        if m.get('ElasticityAssuranceRenewAttribute') is not None:
            for k1 in m.get('ElasticityAssuranceRenewAttribute'):
                temp_model = main_models.DescribeElasticityAssuranceAutoRenewAttributeResponseBodyElasticityAssuranceRenewAttributesElasticityAssuranceRenewAttribute()
                self.elasticity_assurance_renew_attribute.append(temp_model.from_map(k1))

        return self

class DescribeElasticityAssuranceAutoRenewAttributeResponseBodyElasticityAssuranceRenewAttributesElasticityAssuranceRenewAttribute(DaraModel):
    def __init__(
        self,
        period: int = None,
        period_unit: str = None,
        private_pool_options_id: str = None,
        renewal_status: str = None,
    ):
        # The auto-renewal period. Valid values: Valid values: 1, 2, 3, 6, 12, 24, and 36.
        self.period = period
        # The unit of the auto-renewal period. Valid values:
        # 
        # *   Month (default)
        # *   Year
        self.period_unit = period_unit
        # The ID of the elasticity assurance.
        self.private_pool_options_id = private_pool_options_id
        # Indicates whether auto-renewal is enabled for the elasticity assurance. Valid values:
        # 
        # *   AutoRenewal: Auto-renewal is enabled for the elasticity assurance.
        # *   Normal: Auto-renewal is disabled for the elasticity assurance.
        # *   NotRenewal: The elasticity assurance is not renewed.
        self.renewal_status = renewal_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.private_pool_options_id is not None:
            result['PrivatePoolOptionsId'] = self.private_pool_options_id

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PrivatePoolOptionsId') is not None:
            self.private_pool_options_id = m.get('PrivatePoolOptionsId')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        return self

