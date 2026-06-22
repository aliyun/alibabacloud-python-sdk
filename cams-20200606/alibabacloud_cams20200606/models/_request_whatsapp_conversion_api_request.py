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
        # The space ID or instance ID of the customer.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # The PageId of Meta.
        # 
        # This parameter is required.
        self.page_id = page_id
        # The request data.
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
        # Specifies where the conversion occurred. Knowing where the event occurred helps ensure that ads are delivered to the correct audience. By using the Conversions API, you agree that the action_source parameter is accurate to the best of your knowledge.
        # 
        # 
        # The values you can send in the action_source field are as follows:
        # 
        # 
        # - email: The conversion occurred through email.
        # - website: The conversion was made on a website.
        # - app: The conversion was made on a shift application.
        # - phone_call: The conversion was made over the phone.
        # - chat: The conversion was made through a messaging app, SMS, or online messaging feature.
        # - physical_store: The conversion was made in person at a physical store entity.
        # - system_generated: The conversion occurred automatically, such as a subscribe renewal with Settings for monthly automatic payment.
        # - other: The conversion was made through a method not listed in this topic.
        # 
        # Note: All action source values support ads measurement and custom audience creation. All action sources except physical_store support ads optimization.
        # 
        # This parameter is required.
        self.action_source = action_source
        # Required parameters for app events.
        # 
        # These parameters are used to share app data and device information with the Conversions API.
        self.app_data = app_data
        # A map that contains additional business data for the event.
        self.custom_data = custom_data
        # The processing options you want to enable for a specific event. For Limited Data Use, the currently accepted value is LDU. You can send an empty array to explicitly specify that the event must not be processed with Limited Data Use restrictions.
        self.data_processing_options = data_processing_options
        # Required if you send LDU under data_processing_options.
        # The country you want to associate with this data processing option. Currently accepted values are 1 (representing the United States) or 0 (requesting that we geolocate this event).
        self.data_processing_options_country = data_processing_options_country
        # Required in some cases. (See the notes below for details.)
        # The state you want to associate with this data processing option. Currently accepted values are 1000 (representing California) or 0 (requesting that we geolocate this event).
        self.data_processing_options_state = data_processing_options_state
        # This ID can be any unique string chosen by the advertiser. The event_name and event_id parameters are used to deduplicate events sent by a website (through Meta Pixel), an app (through the SDK or App Events API), and the Conversions API. Although event_id is marked as optional, we recommend that you use this parameter for deduplication.
        self.event_id = event_id
        # - The name of a standard event or custom event. This field is used to deduplicate events sent by a website (through Meta Pixel), an app (through the SDK or App Events API), and the Conversions API. The event_id parameter is also used for deduplication.
        # 
        # - For the same customer action, the event from the browser or app should match the event_name from the server event. If a match is found between events sent within 48 hours, only the first event is considered. If server and browser/app events are received at approximately the same time (within 5 minutes of each other), the browser/app event takes priority. Learn more about deduplicating Pixel events and server events.
        # 
        # This parameter is required.
        self.event_name = event_name
        # The browser URL where the event occurred. The URL must start with http:// or https:// and should match the verified domain.
        self.event_source_url = event_source_url
        # A Unix timestamp in seconds indicating when the event actually occurred. The specified time may be earlier than the time you send the event to Facebook. This is intended for batch processing and server performance optimization. You must send the date in Greenwich Mean Time (GMT) time zone format.
        # 
        # This parameter is required.
        self.event_time = event_time
        # Required parameters for app events.
        # 
        # Extended device information, such as the width and height of the screen. This parameter is an array with values separated by commas. When using extinfo, all values are required and must be arranged in the following index order. If a value is missing, use an empty string as a placeholder.
        self.ext_info = ext_info
        # The source. Fixed value: whatsapp.
        self.messaging_channel = messaging_channel
        # A flag that indicates this event should not be used for ad delivery optimization. When set to true, the event can only be used for attribution.
        self.opt_out = opt_out
        # A map that contains customer information data.
        # 
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

