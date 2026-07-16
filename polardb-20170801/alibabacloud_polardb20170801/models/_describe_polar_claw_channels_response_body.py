# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawChannelsResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        channels: List[main_models.DescribePolarClawChannelsResponseBodyChannels] = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # A list of PolarClaw channel objects.
        self.channels = channels
        # The returned status code.
        self.code = code
        # The response message. A value of `successful` indicates that the request succeeded.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.channels:
            for v1 in self.channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        result['Channels'] = []
        if self.channels is not None:
            for k1 in self.channels:
                result['Channels'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        self.channels = []
        if m.get('Channels') is not None:
            for k1 in m.get('Channels'):
                temp_model = main_models.DescribePolarClawChannelsResponseBodyChannels()
                self.channels.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePolarClawChannelsResponseBodyChannels(DaraModel):
    def __init__(
        self,
        accounts: List[main_models.DescribePolarClawChannelsResponseBodyChannelsAccounts] = None,
        channel_id: str = None,
        configured: bool = None,
        default_account_id: str = None,
        enabled: bool = None,
    ):
        # A list of account objects for the channel.
        self.accounts = accounts
        # The channel ID.
        self.channel_id = channel_id
        # Indicates whether the channel is configured.
        self.configured = configured
        # The default account ID for the channel.
        self.default_account_id = default_account_id
        # Indicates whether the channel is enabled.
        self.enabled = enabled

    def validate(self):
        if self.accounts:
            for v1 in self.accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Accounts'] = []
        if self.accounts is not None:
            for k1 in self.accounts:
                result['Accounts'].append(k1.to_map() if k1 else None)

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.configured is not None:
            result['Configured'] = self.configured

        if self.default_account_id is not None:
            result['DefaultAccountId'] = self.default_account_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.DescribePolarClawChannelsResponseBodyChannelsAccounts()
                self.accounts.append(temp_model.from_map(k1))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Configured') is not None:
            self.configured = m.get('Configured')

        if m.get('DefaultAccountId') is not None:
            self.default_account_id = m.get('DefaultAccountId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class DescribePolarClawChannelsResponseBodyChannelsAccounts(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        configured: bool = None,
        connected: bool = None,
        enabled: bool = None,
        issues: List[str] = None,
        last_inbound_at: int = None,
        last_outbound_at: int = None,
    ):
        # The account ID.
        self.account_id = account_id
        # Indicates whether the account is configured.
        self.configured = configured
        # Indicates whether the account is connected.
        self.connected = connected
        # Indicates whether the account is enabled.
        self.enabled = enabled
        # A list of issues related to the account.
        self.issues = issues
        # The timestamp (in milliseconds) of the last inbound message.
        self.last_inbound_at = last_inbound_at
        # The timestamp (in milliseconds) of the last outbound message.
        self.last_outbound_at = last_outbound_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.configured is not None:
            result['Configured'] = self.configured

        if self.connected is not None:
            result['Connected'] = self.connected

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.issues is not None:
            result['Issues'] = self.issues

        if self.last_inbound_at is not None:
            result['LastInboundAt'] = self.last_inbound_at

        if self.last_outbound_at is not None:
            result['LastOutboundAt'] = self.last_outbound_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Configured') is not None:
            self.configured = m.get('Configured')

        if m.get('Connected') is not None:
            self.connected = m.get('Connected')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Issues') is not None:
            self.issues = m.get('Issues')

        if m.get('LastInboundAt') is not None:
            self.last_inbound_at = m.get('LastInboundAt')

        if m.get('LastOutboundAt') is not None:
            self.last_outbound_at = m.get('LastOutboundAt')

        return self

