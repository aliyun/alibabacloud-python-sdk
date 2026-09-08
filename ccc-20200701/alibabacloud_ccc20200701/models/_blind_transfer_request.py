# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BlindTransferRequest(DaraModel):
    def __init__(
        self,
        call_priority: int = None,
        contact_flow_variables: str = None,
        device_id: str = None,
        instance_id: str = None,
        job_id: str = None,
        queuing_overflow_threshold: int = None,
        queuing_timeout_seconds: int = None,
        routing_type: str = None,
        skill_group_id: str = None,
        strategy_name: str = None,
        strategy_params: str = None,
        tags: str = None,
        timeout_seconds: int = None,
        transferee: str = None,
        transferee_type: str = None,
        transferor: str = None,
        user_id: str = None,
    ):
        # The queue priority when transferring to a skill group. Valid values are 0–9, where 0 is the highest priority and 9 is the lowest.
        self.call_priority = call_priority
        # Variables passed to the contact flow. This field is optional. The variables configured here can be retrieved and used in the IVR flow. The format is a JSON string representing a set of key-value pairs.
        self.contact_flow_variables = contact_flow_variables
        # Device ID. This parameter is meaningless and can be filled with any value.
        self.device_id = device_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The call ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The queuing overflow threshold when the transfer target is a skill group queue. The default value is 0, which means no overflow occurs.
        self.queuing_overflow_threshold = queuing_overflow_threshold
        # The queuing timeout duration in seconds when the transfer target is a skill group queue.
        self.queuing_timeout_seconds = queuing_timeout_seconds
        # The call routing type. Valid values are Automatic or Manual. If this parameter is empty, the system defaults to Automatic routing, which is also the current default behavior of the system. When Manual routing is selected, you must invoke APIs such as ClaimCall to assign the call to a specific agent.
        self.routing_type = routing_type
        # Skill group ID.
        self.skill_group_id = skill_group_id
        # The policy name for agent assignment when transferring to a skill group queue.
        self.strategy_name = strategy_name
        # The parameters for the agent assignment policy when transferring to a skill group queue.
        self.strategy_params = strategy_params
        # Ingest endpoint data, primarily used for extension purposes. Regular users do not need to concern themselves with this field.
        self.tags = tags
        # Timeout duration for the direct transfer, in seconds. If the transferee does not answer within the specified time, the call is disconnected. This field is optional and defaults to 30 seconds.
        self.timeout_seconds = timeout_seconds
        # The transfer recipient, which can be either an agent ID or a skill group ID.
        # 
        # This parameter is required.
        self.transferee = transferee
        # Destination type for the transfer. Valid values are AGENT, SKILL_GROUP, IVR, and EXTERNAL_NUMBER. If this parameter is not specified, the system determines the destination type based on the format of the target number. If the automatic detection is inaccurate, you must explicitly specify this parameter.
        self.transferee_type = transferee_type
        # The transfer initiator. When the scenario involves directly transferring to an external number, the number specified by this parameter is used as the caller. This parameter is invalid when transferring to an internal agent or skill group; in such cases, the initiator is specified by the UserId parameter.
        self.transferor = transferor
        # The agent ID that initiates a direct transfer.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_priority is not None:
            result['CallPriority'] = self.call_priority

        if self.contact_flow_variables is not None:
            result['ContactFlowVariables'] = self.contact_flow_variables

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.queuing_overflow_threshold is not None:
            result['QueuingOverflowThreshold'] = self.queuing_overflow_threshold

        if self.queuing_timeout_seconds is not None:
            result['QueuingTimeoutSeconds'] = self.queuing_timeout_seconds

        if self.routing_type is not None:
            result['RoutingType'] = self.routing_type

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.strategy_params is not None:
            result['StrategyParams'] = self.strategy_params

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        if self.transferee is not None:
            result['Transferee'] = self.transferee

        if self.transferee_type is not None:
            result['TransfereeType'] = self.transferee_type

        if self.transferor is not None:
            result['Transferor'] = self.transferor

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallPriority') is not None:
            self.call_priority = m.get('CallPriority')

        if m.get('ContactFlowVariables') is not None:
            self.contact_flow_variables = m.get('ContactFlowVariables')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('QueuingOverflowThreshold') is not None:
            self.queuing_overflow_threshold = m.get('QueuingOverflowThreshold')

        if m.get('QueuingTimeoutSeconds') is not None:
            self.queuing_timeout_seconds = m.get('QueuingTimeoutSeconds')

        if m.get('RoutingType') is not None:
            self.routing_type = m.get('RoutingType')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('StrategyParams') is not None:
            self.strategy_params = m.get('StrategyParams')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        if m.get('Transferee') is not None:
            self.transferee = m.get('Transferee')

        if m.get('TransfereeType') is not None:
            self.transferee_type = m.get('TransfereeType')

        if m.get('Transferor') is not None:
            self.transferor = m.get('Transferor')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

