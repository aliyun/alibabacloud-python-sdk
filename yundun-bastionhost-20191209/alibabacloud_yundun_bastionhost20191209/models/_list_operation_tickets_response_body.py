# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListOperationTicketsResponseBody(DaraModel):
    def __init__(
        self,
        operation_tickets: List[main_models.ListOperationTicketsResponseBodyOperationTickets] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The O\\&M applications to be reviewed.
        self.operation_tickets = operation_tickets
        # The request ID.
        self.request_id = request_id
        # The total number of O\\&M applications to be reviewed.
        self.total_count = total_count

    def validate(self):
        if self.operation_tickets:
            for v1 in self.operation_tickets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperationTickets'] = []
        if self.operation_tickets is not None:
            for k1 in self.operation_tickets:
                result['OperationTickets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation_tickets = []
        if m.get('OperationTickets') is not None:
            for k1 in m.get('OperationTickets'):
                temp_model = main_models.ListOperationTicketsResponseBodyOperationTickets()
                self.operation_tickets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOperationTicketsResponseBodyOperationTickets(DaraModel):
    def __init__(
        self,
        apply_user_id: str = None,
        apply_username: str = None,
        approve_comment: str = None,
        asset_account_id: str = None,
        asset_account_name: str = None,
        asset_address: str = None,
        asset_id: str = None,
        asset_name: str = None,
        asset_network_domain_id: str = None,
        asset_os: str = None,
        asset_source: str = None,
        asset_source_instance_id: str = None,
        created_time: int = None,
        effect_count: int = None,
        effect_end_time: int = None,
        effect_start_time: int = None,
        operation_ticket_id: str = None,
        protocol_name: str = None,
        state: str = None,
    ):
        # The ID of the O\\&M applicant.
        self.apply_user_id = apply_user_id
        # The username of the O\\&M applicant.
        self.apply_username = apply_username
        # The remarks entered when the O\\&M personnel applies for O\\&M permissions.
        self.approve_comment = approve_comment
        # The ID of the asset account.
        self.asset_account_id = asset_account_id
        # The username of the asset account.
        self.asset_account_name = asset_account_name
        # The IP address of the asset.
        self.asset_address = asset_address
        # The ID of the asset.
        self.asset_id = asset_id
        # The name of the asset.
        self.asset_name = asset_name
        # The network domain ID of the asset.
        self.asset_network_domain_id = asset_network_domain_id
        # The operating system of the asset.
        self.asset_os = asset_os
        # The name of the asset source to which the asset belongs. Valid values:
        # 
        # *   **Local**: an on-premises host.
        # *   **Ecs**: an Elastic Compute Service (ECS) instance.
        # *   **Rds**: an ApsaraDB RDS instance.
        # *   A third-party asset source.
        self.asset_source = asset_source
        # The ID of the asset source to which the asset belongs.
        self.asset_source_instance_id = asset_source_instance_id
        # The time when the O\\&M application was submitted. The value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The maximum number of logons applied by the O\\&M engineer. Valid values:
        # 
        # *   **0**: The number of logons is unlimited. The O\\&M engineer can log on to the specified asset for unlimited times during the validity period.
        # *   **1**: The O\\&M engineer can log on to the specified asset only once during the validity period.
        self.effect_count = effect_count
        # The end time of the validity period. The value is a UNIX timestamp. Unit: seconds.
        self.effect_end_time = effect_end_time
        # The start time of the validity period. The value is a UNIX timestamp. Unit: seconds.
        self.effect_start_time = effect_start_time
        # The ID of the O\\&M application to be reviewed.
        self.operation_ticket_id = operation_ticket_id
        # The O\\&M protocol.
        self.protocol_name = protocol_name
        # The status of the review. Valid value:
        # 
        # *   Normal: to be reviewed
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_user_id is not None:
            result['ApplyUserId'] = self.apply_user_id

        if self.apply_username is not None:
            result['ApplyUsername'] = self.apply_username

        if self.approve_comment is not None:
            result['ApproveComment'] = self.approve_comment

        if self.asset_account_id is not None:
            result['AssetAccountId'] = self.asset_account_id

        if self.asset_account_name is not None:
            result['AssetAccountName'] = self.asset_account_name

        if self.asset_address is not None:
            result['AssetAddress'] = self.asset_address

        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.asset_network_domain_id is not None:
            result['AssetNetworkDomainId'] = self.asset_network_domain_id

        if self.asset_os is not None:
            result['AssetOs'] = self.asset_os

        if self.asset_source is not None:
            result['AssetSource'] = self.asset_source

        if self.asset_source_instance_id is not None:
            result['AssetSourceInstanceId'] = self.asset_source_instance_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.effect_count is not None:
            result['EffectCount'] = self.effect_count

        if self.effect_end_time is not None:
            result['EffectEndTime'] = self.effect_end_time

        if self.effect_start_time is not None:
            result['EffectStartTime'] = self.effect_start_time

        if self.operation_ticket_id is not None:
            result['OperationTicketId'] = self.operation_ticket_id

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyUserId') is not None:
            self.apply_user_id = m.get('ApplyUserId')

        if m.get('ApplyUsername') is not None:
            self.apply_username = m.get('ApplyUsername')

        if m.get('ApproveComment') is not None:
            self.approve_comment = m.get('ApproveComment')

        if m.get('AssetAccountId') is not None:
            self.asset_account_id = m.get('AssetAccountId')

        if m.get('AssetAccountName') is not None:
            self.asset_account_name = m.get('AssetAccountName')

        if m.get('AssetAddress') is not None:
            self.asset_address = m.get('AssetAddress')

        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('AssetNetworkDomainId') is not None:
            self.asset_network_domain_id = m.get('AssetNetworkDomainId')

        if m.get('AssetOs') is not None:
            self.asset_os = m.get('AssetOs')

        if m.get('AssetSource') is not None:
            self.asset_source = m.get('AssetSource')

        if m.get('AssetSourceInstanceId') is not None:
            self.asset_source_instance_id = m.get('AssetSourceInstanceId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('EffectCount') is not None:
            self.effect_count = m.get('EffectCount')

        if m.get('EffectEndTime') is not None:
            self.effect_end_time = m.get('EffectEndTime')

        if m.get('EffectStartTime') is not None:
            self.effect_start_time = m.get('EffectStartTime')

        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

