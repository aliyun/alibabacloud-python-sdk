# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListInstagramPageResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.ListInstagramPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListInstagramPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInstagramPageResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_info: main_models.ListInstagramPageResponseBodyDataAgentInfo = None,
        beebot_info: main_models.ListInstagramPageResponseBodyDataBeebotInfo = None,
        instagram_info: main_models.ListInstagramPageResponseBodyDataInstagramInfo = None,
    ):
        self.agent_info = agent_info
        self.beebot_info = beebot_info
        self.instagram_info = instagram_info

    def validate(self):
        if self.agent_info:
            self.agent_info.validate()
        if self.beebot_info:
            self.beebot_info.validate()
        if self.instagram_info:
            self.instagram_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_info is not None:
            result['AgentInfo'] = self.agent_info.to_map()

        if self.beebot_info is not None:
            result['BeebotInfo'] = self.beebot_info.to_map()

        if self.instagram_info is not None:
            result['InstagramInfo'] = self.instagram_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentInfo') is not None:
            temp_model = main_models.ListInstagramPageResponseBodyDataAgentInfo()
            self.agent_info = temp_model.from_map(m.get('AgentInfo'))

        if m.get('BeebotInfo') is not None:
            temp_model = main_models.ListInstagramPageResponseBodyDataBeebotInfo()
            self.beebot_info = temp_model.from_map(m.get('BeebotInfo'))

        if m.get('InstagramInfo') is not None:
            temp_model = main_models.ListInstagramPageResponseBodyDataInstagramInfo()
            self.instagram_info = temp_model.from_map(m.get('InstagramInfo'))

        return self

class ListInstagramPageResponseBodyDataInstagramInfo(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        connection_status: str = None,
        http_flag: str = None,
        page_id: str = None,
        page_name: str = None,
        queue_flag: str = None,
        queue_name: str = None,
        status_callback_url: str = None,
        status_queue: str = None,
        up_callback_url: str = None,
        up_queue: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.connection_status = connection_status
        self.http_flag = http_flag
        self.page_id = page_id
        self.page_name = page_name
        self.queue_flag = queue_flag
        self.queue_name = queue_name
        self.status_callback_url = status_callback_url
        self.status_queue = status_queue
        self.up_callback_url = up_callback_url
        self.up_queue = up_queue

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.http_flag is not None:
            result['HttpFlag'] = self.http_flag

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.page_name is not None:
            result['PageName'] = self.page_name

        if self.queue_flag is not None:
            result['QueueFlag'] = self.queue_flag

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url

        if self.status_queue is not None:
            result['StatusQueue'] = self.status_queue

        if self.up_callback_url is not None:
            result['UpCallbackUrl'] = self.up_callback_url

        if self.up_queue is not None:
            result['UpQueue'] = self.up_queue

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('HttpFlag') is not None:
            self.http_flag = m.get('HttpFlag')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('PageName') is not None:
            self.page_name = m.get('PageName')

        if m.get('QueueFlag') is not None:
            self.queue_flag = m.get('QueueFlag')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')

        if m.get('StatusQueue') is not None:
            self.status_queue = m.get('StatusQueue')

        if m.get('UpCallbackUrl') is not None:
            self.up_callback_url = m.get('UpCallbackUrl')

        if m.get('UpQueue') is not None:
            self.up_queue = m.get('UpQueue')

        return self

class ListInstagramPageResponseBodyDataBeebotInfo(DaraModel):
    def __init__(
        self,
        beebot_instance_id: str = None,
        beebot_namespace_id: str = None,
    ):
        self.beebot_instance_id = beebot_instance_id
        self.beebot_namespace_id = beebot_namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.beebot_instance_id is not None:
            result['BeebotInstanceId'] = self.beebot_instance_id

        if self.beebot_namespace_id is not None:
            result['BeebotNamespaceId'] = self.beebot_namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeebotInstanceId') is not None:
            self.beebot_instance_id = m.get('BeebotInstanceId')

        if m.get('BeebotNamespaceId') is not None:
            self.beebot_namespace_id = m.get('BeebotNamespaceId')

        return self

class ListInstagramPageResponseBodyDataAgentInfo(DaraModel):
    def __init__(
        self,
        agent_keywords: str = None,
        agent_no_keywords: str = None,
    ):
        self.agent_keywords = agent_keywords
        self.agent_no_keywords = agent_no_keywords

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_keywords is not None:
            result['AgentKeywords'] = self.agent_keywords

        if self.agent_no_keywords is not None:
            result['AgentNoKeywords'] = self.agent_no_keywords

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKeywords') is not None:
            self.agent_keywords = m.get('AgentKeywords')

        if m.get('AgentNoKeywords') is not None:
            self.agent_no_keywords = m.get('AgentNoKeywords')

        return self

