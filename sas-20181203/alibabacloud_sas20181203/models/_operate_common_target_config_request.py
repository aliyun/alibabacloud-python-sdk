# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateCommonTargetConfigRequest(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
        source_ip: str = None,
        target_operations: str = None,
        target_type: str = None,
        type: str = None,
    ):
        # The type of the image. Valid values:
        # 
        # *   **repoName**: the name of the image repository
        # *   **repoNamespace**: the namespace of the image repository
        self.field_name = field_name
        # The name of the image repository or the namespace of the image repository.
        self.field_value = field_value
        # The source IP address of the request.
        self.source_ip = source_ip
        # The configuration of proactive defense for your server. The value includes the following fields:
        # 
        # *   **targetType**: specifies the dimension from which you manage proactive defense. UUIDs are supported. Set the value to **uuid**.
        # *   **target**: specifies the UUID of the server for which you want to configure proactive defense.
        # *   **flag**: specifies whether to enable or disable proactive defense for your server. Valid values are **add** and **del**. The value add indicates that proactive defense will be enabled for your server. The value del indicates that proactive defense will be disabled for your server.
        # 
        # This parameter is required.
        self.target_operations = target_operations
        # The dimension based on which the asset is selected. Valid values:
        # 
        # *   **uuid**: the UUID of the server
        # *   **Cluster**: the ID of the cluster
        # *   **image_repo**: the name of the image repository
        self.target_type = target_type
        # The type of the feature. Valid values:
        # 
        # *   **alidetect-scan-enable**: local file detection
        # *   **ACTION-TRIAL-PERMISSION**: data delivery to ActionTrail
        # *   **alidetect**: local file detection engine
        # *   **container_prevent_escape**: container escape prevention
        # *   **image_repo**: repository image scan
        # *   **proc_filter_switch**: log filtering
        # *   **agentless**: agentless detection
        # *   **rasp**: application protection
        # *   **sensitiveFile**: sensitive file detection
        # *   **aliscriptengine**: in-depth detection engine
        # *   **containerNetwork**: container network visualization
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.target_operations is not None:
            result['TargetOperations'] = self.target_operations

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TargetOperations') is not None:
            self.target_operations = m.get('TargetOperations')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

