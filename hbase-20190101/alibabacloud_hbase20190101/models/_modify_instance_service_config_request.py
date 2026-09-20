# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceServiceConfigRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        configure_name: str = None,
        configure_value: str = None,
        parameters: str = None,
        restart: bool = None,
    ):
        # The ID of target instance. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) operation to obtain target instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # <props="china">The name of the configuration item to modify. You can call the [ListInstanceServiceConfigurations](https://help.aliyun.com/document_detail/201980.html) operation to query the configuration item name.
        # <props="intl">The name of the configuration item to modify.
        # 
        # > If you want to modify multiple configuration items, specify the Parameters parameter.
        # 
        # This parameter is required.
        self.configure_name = configure_name
        # <props="china">The value of the configuration item to modify. You can call the [ListInstanceServiceConfigurations](https://help.aliyun.com/document_detail/201980.html) operation to query the configuration item value.
        # <props="intl">The value of the configuration item to modify.
        # 
        # > If you want to modify multiple configuration items, specify the Parameters parameter.
        # 
        # This parameter is required.
        self.configure_value = configure_value
        # The JSON-formatted parameters for modifying multiple configuration items. The key specifies the name of the configuration item, and the value specifies the value of the configuration item.
        self.parameters = parameters
        # Specifies whether to restart the instance after the configuration is modified. Valid values:
        # 
        # - **true**: Restart the instance.
        # - **false**: Do not restart the instance.
        self.restart = restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.configure_name is not None:
            result['ConfigureName'] = self.configure_name

        if self.configure_value is not None:
            result['ConfigureValue'] = self.configure_value

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.restart is not None:
            result['Restart'] = self.restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConfigureName') is not None:
            self.configure_name = m.get('ConfigureName')

        if m.get('ConfigureValue') is not None:
            self.configure_value = m.get('ConfigureValue')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        return self

