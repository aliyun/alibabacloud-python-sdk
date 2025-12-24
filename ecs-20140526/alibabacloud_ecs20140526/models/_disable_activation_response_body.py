# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DisableActivationResponseBody(DaraModel):
    def __init__(
        self,
        activation: main_models.DisableActivationResponseBodyActivation = None,
        request_id: str = None,
    ):
        # The time when the activation code was created.
        self.activation = activation
        # Details about the activation code and its usage information.
        self.request_id = request_id

    def validate(self):
        if self.activation:
            self.activation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation is not None:
            result['Activation'] = self.activation.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Activation') is not None:
            temp_model = main_models.DisableActivationResponseBodyActivation()
            self.activation = temp_model.from_map(m.get('Activation'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DisableActivationResponseBodyActivation(DaraModel):
    def __init__(
        self,
        activation_id: str = None,
        creation_time: str = None,
        deregistered_count: int = None,
        description: str = None,
        disabled: bool = None,
        instance_count: int = None,
        instance_name: str = None,
        ip_address_range: str = None,
        registered_count: int = None,
        time_to_live_in_hours: int = None,
    ):
        # The ID of the activation code.
        self.activation_id = activation_id
        # The number of instances that were deregistered.
        self.creation_time = creation_time
        # The maximum number of times that the activation code can be used to register managed instances.
        self.deregistered_count = deregistered_count
        # The number of registered instances.
        self.description = description
        # The IP addresses of the hosts that can use the activation code.
        self.disabled = disabled
        # The description of the activation code.
        self.instance_count = instance_count
        # Indicates whether the activation code is disabled.
        self.instance_name = instance_name
        # The validity period of the activation code. Unit: hours.
        self.ip_address_range = ip_address_range
        # The default prefix of the instance name.
        self.registered_count = registered_count
        # The activation code ID.
        self.time_to_live_in_hours = time_to_live_in_hours

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation_id is not None:
            result['ActivationId'] = self.activation_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.deregistered_count is not None:
            result['DeregisteredCount'] = self.deregistered_count

        if self.description is not None:
            result['Description'] = self.description

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.ip_address_range is not None:
            result['IpAddressRange'] = self.ip_address_range

        if self.registered_count is not None:
            result['RegisteredCount'] = self.registered_count

        if self.time_to_live_in_hours is not None:
            result['TimeToLiveInHours'] = self.time_to_live_in_hours

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationId') is not None:
            self.activation_id = m.get('ActivationId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeregisteredCount') is not None:
            self.deregistered_count = m.get('DeregisteredCount')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IpAddressRange') is not None:
            self.ip_address_range = m.get('IpAddressRange')

        if m.get('RegisteredCount') is not None:
            self.registered_count = m.get('RegisteredCount')

        if m.get('TimeToLiveInHours') is not None:
            self.time_to_live_in_hours = m.get('TimeToLiveInHours')

        return self

