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
        # The target type of the image switch. Valid values:
        # - **repoName**: repository name.
        # - **repoNamespace**: repository namespace name.
        self.field_name = field_name
        # The repository name or repository namespace name.
        self.field_value = field_value
        # The IP address of the access source.
        self.source_ip = source_ip
        # The parameters for configuring proactive defense on servers. The following parameters are included:
        # 
        # - **targetType**: the dimension of the defense configuration. Currently, only the UUID dimension is supported. Fixed value: **uuid**.
        # - **target**: the UUID of the server for which you want to configure proactive defense.
        # - **flag**: specifies whether to enable or disable proactive defense for the server. Valid values: **add** (enable) and **del** (disable).
        # 
        # This parameter is required.
        self.target_operations = target_operations
        # The Asset Type of the target. Valid values:
        # - **uuid**: server UUID.
        # - **Cluster**: cluster ID.
        # - **image_repo**: image repository name.
        self.target_type = target_type
        # The switch type. Valid values:
        # - **alidetect-scan-enable**: local file detection that performs detection only locally.
        # - **ACTION-TRIAL-PERMISSION**: ActionTrail data delivery.
        # - **alidetect**: local file detection engine.
        # - **container_prevent_escape**: container escape prevention.
        # - **image_repo**: repository image scanning.
        # - **proc_filter_switch**: log filtering.
        # - **agentless**: agentless detection.
        # - **rasp**: application protection.
        # - **sensitiveFile**: sensitive information scanning.
        # - **aliscriptengine**: deep detection engine.
        # - **containerNetwork**: container visualization.
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

