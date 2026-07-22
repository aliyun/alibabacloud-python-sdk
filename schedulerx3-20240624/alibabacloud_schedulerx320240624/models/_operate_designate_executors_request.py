# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OperateDesignateExecutorsRequest(DaraModel):
    def __init__(
        self,
        address_list: List[str] = None,
        app_group_id: int = None,
        app_name: str = None,
        cluster_id: str = None,
        designate_type: int = None,
        job_id: int = None,
        transferable: bool = None,
    ):
        # The address list.
        # 
        # This parameter is required.
        self.address_list = address_list
        self.app_group_id = app_group_id
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The type of the designated machine. Valid values:
        # - **1**: designated worker.
        # - **2**: designated label.
        # 
        # This parameter is required.
        self.designate_type = designate_type
        # The task ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Specifies whether to enable failover.
        self.transferable = transferable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_list is not None:
            result['AddressList'] = self.address_list

        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.designate_type is not None:
            result['DesignateType'] = self.designate_type

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.transferable is not None:
            result['Transferable'] = self.transferable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')

        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DesignateType') is not None:
            self.designate_type = m.get('DesignateType')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Transferable') is not None:
            self.transferable = m.get('Transferable')

        return self

