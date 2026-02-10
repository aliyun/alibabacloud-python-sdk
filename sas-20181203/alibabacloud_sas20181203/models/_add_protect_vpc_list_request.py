# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddProtectVpcListRequest(DaraModel):
    def __init__(
        self,
        add_vpc_instance_id_list: str = None,
        del_vpc_instance_id_list: str = None,
    ):
        # Collection of new VPC instance IDs.
        # > Call the [DescribeVpcList](~~DescribeVpcList~~) interface to obtain this parameter.
        self.add_vpc_instance_id_list = add_vpc_instance_id_list
        # Collection of VPC instance IDs to be deleted.
        # > Call the [DescribeVpcList](~~DescribeVpcList~~) interface to obtain this parameter.
        self.del_vpc_instance_id_list = del_vpc_instance_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_vpc_instance_id_list is not None:
            result['AddVpcInstanceIdList'] = self.add_vpc_instance_id_list

        if self.del_vpc_instance_id_list is not None:
            result['DelVpcInstanceIdList'] = self.del_vpc_instance_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddVpcInstanceIdList') is not None:
            self.add_vpc_instance_id_list = m.get('AddVpcInstanceIdList')

        if m.get('DelVpcInstanceIdList') is not None:
            self.del_vpc_instance_id_list = m.get('DelVpcInstanceIdList')

        return self

