# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class RequestWhatsappConversionApiRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        owner_id: int = None,
        page_id: str = None,
        request_data: List[main_models.RequestWhatsappConversionApiRequestRequestData] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.page_id = page_id
        self.request_data = request_data
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.request_data:
            for v1 in self.request_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_id is not None:
            result['PageId'] = self.page_id

        result['RequestData'] = []
        if self.request_data is not None:
            for k1 in self.request_data:
                result['RequestData'].append(k1.to_map() if k1 else None)

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        self.request_data = []
        if m.get('RequestData') is not None:
            for k1 in m.get('RequestData'):
                temp_model = main_models.RequestWhatsappConversionApiRequestRequestData()
                self.request_data.append(temp_model.from_map(k1))

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class RequestWhatsappConversionApiRequestRequestData(DaraModel):
    def __init__(
        self,
        action_source: str = None,
        app_data: Dict[str, Any] = None,
        custom_data: Dict[str, Any] = None,
        data_processing_options: List[str] = None,
        data_processing_options_country: int = None,
        data_processing_options_state: int = None,
        event_id: str = None,
        event_name: str = None,
        event_source_url: str = None,
        event_time: int = None,
        ext_info: Dict[str, Any] = None,
        messaging_channel: str = None,
        opt_out: bool = None,
        user_data: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.action_source = action_source
        self.app_data = app_data
        self.custom_data = custom_data
        self.data_processing_options = data_processing_options
        self.data_processing_options_country = data_processing_options_country
        self.data_processing_options_state = data_processing_options_state
        self.event_id = event_id
        # This parameter is required.
        self.event_name = event_name
        self.event_source_url = event_source_url
        # This parameter is required.
        self.event_time = event_time
        self.ext_info = ext_info
        self.messaging_channel = messaging_channel
        self.opt_out = opt_out
        # This parameter is required.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_source is not None:
            result['ActionSource'] = self.action_source

        if self.app_data is not None:
            result['AppData'] = self.app_data

        if self.custom_data is not None:
            result['CustomData'] = self.custom_data

        if self.data_processing_options is not None:
            result['DataProcessingOptions'] = self.data_processing_options

        if self.data_processing_options_country is not None:
            result['DataProcessingOptionsCountry'] = self.data_processing_options_country

        if self.data_processing_options_state is not None:
            result['DataProcessingOptionsState'] = self.data_processing_options_state

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_source_url is not None:
            result['EventSourceUrl'] = self.event_source_url

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.messaging_channel is not None:
            result['MessagingChannel'] = self.messaging_channel

        if self.opt_out is not None:
            result['OptOut'] = self.opt_out

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionSource') is not None:
            self.action_source = m.get('ActionSource')

        if m.get('AppData') is not None:
            self.app_data = m.get('AppData')

        if m.get('CustomData') is not None:
            self.custom_data = m.get('CustomData')

        if m.get('DataProcessingOptions') is not None:
            self.data_processing_options = m.get('DataProcessingOptions')

        if m.get('DataProcessingOptionsCountry') is not None:
            self.data_processing_options_country = m.get('DataProcessingOptionsCountry')

        if m.get('DataProcessingOptionsState') is not None:
            self.data_processing_options_state = m.get('DataProcessingOptionsState')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventSourceUrl') is not None:
            self.event_source_url = m.get('EventSourceUrl')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('MessagingChannel') is not None:
            self.messaging_channel = m.get('MessagingChannel')

        if m.get('OptOut') is not None:
            self.opt_out = m.get('OptOut')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

