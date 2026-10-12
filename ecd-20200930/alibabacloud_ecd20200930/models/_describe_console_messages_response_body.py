# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeConsoleMessagesResponseBody(DaraModel):
    def __init__(
        self,
        message_list: List[main_models.DescribeConsoleMessagesResponseBodyMessageList] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of console messages queried on the current page. If no messages match, an empty list is returned.
        self.message_list = message_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of messages that match the query conditions, not the number of messages returned on the current page.
        self.total_count = total_count

    def validate(self):
        if self.message_list:
            for v1 in self.message_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MessageList'] = []
        if self.message_list is not None:
            for k1 in self.message_list:
                result['MessageList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_list = []
        if m.get('MessageList') is not None:
            for k1 in m.get('MessageList'):
                temp_model = main_models.DescribeConsoleMessagesResponseBodyMessageList()
                self.message_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeConsoleMessagesResponseBodyMessageList(DaraModel):
    def __init__(
        self,
        client_types: List[str] = None,
        content_configs: List[main_models.DescribeConsoleMessagesResponseBodyMessageListContentConfigs] = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hyper_link_configs: List[main_models.DescribeConsoleMessagesResponseBodyMessageListHyperLinkConfigs] = None,
        image_file_path: str = None,
        image_info_list: List[main_models.DescribeConsoleMessagesResponseBodyMessageListImageInfoList] = None,
        image_url: str = None,
        message_id: str = None,
        message_level: str = None,
        message_type: str = None,
        meta_data: main_models.DescribeConsoleMessagesResponseBodyMessageListMetaData = None,
        position: str = None,
        start_time: str = None,
        status: str = None,
        target_ids: str = None,
        target_type: str = None,
        title_configs: List[main_models.DescribeConsoleMessagesResponseBodyMessageListTitleConfigs] = None,
    ):
        # The list of client types to which the message applies. Standard names are returned: Windows, Mac, Web, and Hardware.
        self.client_types = client_types
        # The list of message body configurations for each language.
        self.content_configs = content_configs
        # The time when the operational message stops taking effect.
        self.end_time = end_time
        # The time when the message was created.
        self.gmt_create = gmt_create
        # The time when the message was last modified. This time is also updated when the message status changes.
        self.gmt_modified = gmt_modified
        # The list of hyperlink button configurations in the message.
        self.hyper_link_configs = hyper_link_configs
        # The storage path of the image file for the operational message.
        self.image_file_path = image_file_path
        # The list of image configurations, which is mainly used for custom wallpaper messages. Each item includes the image name, image type, storage path, and temporary download URL.
        self.image_info_list = image_info_list
        # The temporary download URL of the operational message image. The link has a limited validity period. If it expires, you can query again to obtain a new one.
        self.image_url = image_url
        # The message ID, which can be used to send, modify, or delete a specified message.
        self.message_id = message_id
        # The message level of the notification message. Valid values: STRONG (strong message) and WEAK (weak message).
        self.message_level = message_level
        # The message type. Valid values: OPERATIONAL (client operational message), WALLPAPER (desktop wallpaper text message), NOTIFICATION (message center notification), and CUSTOM_WALLPAPER (custom desktop wallpaper).
        self.message_type = message_type
        # The additional configuration of the message, including the associated workspace, AD domain name, and scheduled sending configuration. Whether specific fields are returned depends on the message type and its saved configuration.
        self.meta_data = meta_data
        # The display position of the message. For wallpaper text messages, valid values are CENTER (center), TOP_RIGHT (top right), BOTTOM_RIGHT (bottom right), and BOTTOM_LEFT (bottom left). For client operational messages, valid values are CLIENT_ENTERPRISE_RESOURCE_PAGE (Enterprise Edition client cloud resource page) and CLIENT_BUSINESS_RESOURCE_PAGE (Business Edition client cloud resource page).
        self.position = position
        # The time when the operational message starts taking effect.
        self.start_time = start_time
        # The current status of the message. Valid values: Init (initializing), Pushing (pushing), Published (published), Expired (expired), Deleting (deleting), and Failed (failed). Published indicates that the message has been published or the server has finished pushing, but it does not indicate that all target terminals have successfully received the message.
        self.status = status
        # The JSON string of the list of targets to which the message applies. For Organization and AdOrg, it is an array of objects containing orgId (organization ID) and orgName (organization name). The organization name may be empty, and records in the old format may not contain orgName. For Tag, it is an array of objects containing tagKey (tag key), tagValue (tag value), and regionId (region ID). For other target types, it is an array of strings. The target for all users is represented by ALL_USERS.
        self.target_ids = target_ids
        # The type of the target to which the message applies. Valid values: AllUsers (all convenience users), EndUser (specified convenience user), Organization (specified convenience user organization), Desktop (cloud computer), ResourceGroup (resource group), Region (region), Tag (tag), AdAllUsers (all AD users), AdUser (specified AD user), and AdOrg (specified AD organization).
        self.target_type = target_type
        # The list of message title configurations for each language.
        self.title_configs = title_configs

    def validate(self):
        if self.content_configs:
            for v1 in self.content_configs:
                 if v1:
                    v1.validate()
        if self.hyper_link_configs:
            for v1 in self.hyper_link_configs:
                 if v1:
                    v1.validate()
        if self.image_info_list:
            for v1 in self.image_info_list:
                 if v1:
                    v1.validate()
        if self.meta_data:
            self.meta_data.validate()
        if self.title_configs:
            for v1 in self.title_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_types is not None:
            result['ClientTypes'] = self.client_types

        result['ContentConfigs'] = []
        if self.content_configs is not None:
            for k1 in self.content_configs:
                result['ContentConfigs'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        result['HyperLinkConfigs'] = []
        if self.hyper_link_configs is not None:
            for k1 in self.hyper_link_configs:
                result['HyperLinkConfigs'].append(k1.to_map() if k1 else None)

        if self.image_file_path is not None:
            result['ImageFilePath'] = self.image_file_path

        result['ImageInfoList'] = []
        if self.image_info_list is not None:
            for k1 in self.image_info_list:
                result['ImageInfoList'].append(k1.to_map() if k1 else None)

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.message_level is not None:
            result['MessageLevel'] = self.message_level

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data.to_map()

        if self.position is not None:
            result['Position'] = self.position

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        result['TitleConfigs'] = []
        if self.title_configs is not None:
            for k1 in self.title_configs:
                result['TitleConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientTypes') is not None:
            self.client_types = m.get('ClientTypes')

        self.content_configs = []
        if m.get('ContentConfigs') is not None:
            for k1 in m.get('ContentConfigs'):
                temp_model = main_models.DescribeConsoleMessagesResponseBodyMessageListContentConfigs()
                self.content_configs.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        self.hyper_link_configs = []
        if m.get('HyperLinkConfigs') is not None:
            for k1 in m.get('HyperLinkConfigs'):
                temp_model = main_models.DescribeConsoleMessagesResponseBodyMessageListHyperLinkConfigs()
                self.hyper_link_configs.append(temp_model.from_map(k1))

        if m.get('ImageFilePath') is not None:
            self.image_file_path = m.get('ImageFilePath')

        self.image_info_list = []
        if m.get('ImageInfoList') is not None:
            for k1 in m.get('ImageInfoList'):
                temp_model = main_models.DescribeConsoleMessagesResponseBodyMessageListImageInfoList()
                self.image_info_list.append(temp_model.from_map(k1))

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('MessageLevel') is not None:
            self.message_level = m.get('MessageLevel')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('MetaData') is not None:
            temp_model = main_models.DescribeConsoleMessagesResponseBodyMessageListMetaData()
            self.meta_data = temp_model.from_map(m.get('MetaData'))

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        self.title_configs = []
        if m.get('TitleConfigs') is not None:
            for k1 in m.get('TitleConfigs'):
                temp_model = main_models.DescribeConsoleMessagesResponseBodyMessageListTitleConfigs()
                self.title_configs.append(temp_model.from_map(k1))

        return self

class DescribeConsoleMessagesResponseBodyMessageListTitleConfigs(DaraModel):
    def __init__(
        self,
        color: str = None,
        lang_type: str = None,
        title_text: str = None,
    ):
        # The color of the title text, which retains the color value saved when the message was created or modified.
        self.color = color
        # The title language. Valid values: CN (Chinese), EN (English), and JP (Japanese). The query returns the language value saved when the message was created or modified, retaining the original case.
        self.lang_type = lang_type
        # The message title text in the specified language.
        self.title_text = title_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.color is not None:
            result['Color'] = self.color

        if self.lang_type is not None:
            result['LangType'] = self.lang_type

        if self.title_text is not None:
            result['TitleText'] = self.title_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('LangType') is not None:
            self.lang_type = m.get('LangType')

        if m.get('TitleText') is not None:
            self.title_text = m.get('TitleText')

        return self

class DescribeConsoleMessagesResponseBodyMessageListMetaData(DaraModel):
    def __init__(
        self,
        ad_domain: str = None,
        office_site_id: str = None,
        timer: List[str] = None,
        timer_type: str = None,
    ):
        # The AD domain name associated with the message configuration.
        self.ad_domain = ad_domain
        # The workspace ID associated with the message configuration.
        self.office_site_id = office_site_id
        # The list of scheduled sending configurations. If TimerType is CRON, the elements are cron expressions. If TimerType is Timestamp, the elements are millisecond timestamps represented as strings.
        self.timer = timer
        # The scheduled sending type. Valid values: CRON (cron expression) and Timestamp (timestamp). The configuration values are case-sensitive.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.timer is not None:
            result['Timer'] = self.timer

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('Timer') is not None:
            self.timer = m.get('Timer')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

class DescribeConsoleMessagesResponseBodyMessageListImageInfoList(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        image_file_path: str = None,
        image_type: str = None,
        image_url: str = None,
    ):
        # The name of the image file.
        self.file_name = file_name
        # The storage path of the image file.
        self.image_file_path = image_file_path
        # The image type. Configuration types defined by the backend include Operational (operational message image), WallpaperBasic (basic wallpaper image), and WallpaperAppend (appended wallpaper image). The query returns the image type value saved when the message was created or modified, retaining the original case.
        self.image_type = image_type
        # The temporary download URL of the image file. The link has a limited validity period. If it expires, you can query again to obtain a new one.
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.image_file_path is not None:
            result['ImageFilePath'] = self.image_file_path

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('ImageFilePath') is not None:
            self.image_file_path = m.get('ImageFilePath')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        return self

class DescribeConsoleMessagesResponseBodyMessageListHyperLinkConfigs(DaraModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        # The text displayed on the hyperlink button.
        self.title = title
        # The URL accessed after clicking the hyperlink button.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeConsoleMessagesResponseBodyMessageListContentConfigs(DaraModel):
    def __init__(
        self,
        color: str = None,
        content_text: str = None,
        lang_type: str = None,
    ):
        # The color of the body text, which retains the color value saved when the message was created or modified.
        self.color = color
        # The message body text in the specified language.
        self.content_text = content_text
        # The body language. Valid values: CN (Chinese), EN (English), and JP (Japanese). The query returns the language value saved when the message was created or modified, retaining the original case.
        self.lang_type = lang_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.color is not None:
            result['Color'] = self.color

        if self.content_text is not None:
            result['ContentText'] = self.content_text

        if self.lang_type is not None:
            result['LangType'] = self.lang_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')

        if m.get('LangType') is not None:
            self.lang_type = m.get('LangType')

        return self

