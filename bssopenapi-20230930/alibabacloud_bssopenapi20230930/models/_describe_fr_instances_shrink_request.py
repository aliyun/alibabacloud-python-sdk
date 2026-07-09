# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFrInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        capacity_type: str = None,
        commodity_code: str = None,
        cycle_type: str = None,
        ec_id_account_ids_shrink: str = None,
        end_time: int = None,
        group: str = None,
        instance_id: str = None,
        instance_tag: str = None,
        nbid: str = None,
        page_num: int = None,
        page_size: int = None,
        product_code: str = None,
        sort_field: str = None,
        sort_rule: str = None,
        spec: str = None,
        start_time: int = None,
        status: str = None,
        template_code: str = None,
    ):
        # The capacity type.
        self.capacity_type = capacity_type
        # The commodity code.
        self.commodity_code = commodity_code
        # The cycle type.
        self.cycle_type = cycle_type
        # The enterprise and account list. If this parameter is empty, the current account is queried.
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        # The end time.
        self.end_time = end_time
        # The resource dimension to query.
        self.group = group
        # The instance name.
        self.instance_id = instance_id
        # The instance label value of the resource plan.
        self.instance_tag = instance_tag
        # The primary marketplace ID. If this parameter is empty, the marketplace ID of the current user is used by default.
        self.nbid = nbid
        # The current page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The product code.
        self.product_code = product_code
        # The sort field.
        self.sort_field = sort_field
        # The sorting rule.
        self.sort_rule = sort_rule
        # The specification.
        self.spec = spec
        # The start time.
        self.start_time = start_time
        # The resource status.
        self.status = status
        # The template code.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_type is not None:
            result['CapacityType'] = self.capacity_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type

        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_tag is not None:
            result['InstanceTag'] = self.instance_tag

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        if self.sort_rule is not None:
            result['SortRule'] = self.sort_rule

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityType') is not None:
            self.capacity_type = m.get('CapacityType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CycleType') is not None:
            self.cycle_type = m.get('CycleType')

        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceTag') is not None:
            self.instance_tag = m.get('InstanceTag')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        if m.get('SortRule') is not None:
            self.sort_rule = m.get('SortRule')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

