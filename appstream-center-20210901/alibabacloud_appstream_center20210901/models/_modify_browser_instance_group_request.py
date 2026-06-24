# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ModifyBrowserInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        browser_config: main_models.ModifyBrowserInstanceGroupRequestBrowserConfig = None,
        browser_instance_group_id: str = None,
        cloud_browser_name: str = None,
        max_amount: int = None,
        network: main_models.ModifyBrowserInstanceGroupRequestNetwork = None,
        policy: main_models.ModifyBrowserInstanceGroupRequestPolicy = None,
        storage_policy: main_models.ModifyBrowserInstanceGroupRequestStoragePolicy = None,
        timers: List[main_models.ModifyBrowserInstanceGroupRequestTimers] = None,
    ):
        # The browser configuration.
        self.browser_config = browser_config
        # The ID of the cloud browser to modify.
        # 
        # This parameter is required.
        self.browser_instance_group_id = browser_instance_group_id
        # The name of the cloud browser.
        self.cloud_browser_name = cloud_browser_name
        self.max_amount = max_amount
        # The network configuration.
        self.network = network
        # The access policy.
        self.policy = policy
        self.storage_policy = storage_policy
        # The timers.
        self.timers = timers

    def validate(self):
        if self.browser_config:
            self.browser_config.validate()
        if self.network:
            self.network.validate()
        if self.policy:
            self.policy.validate()
        if self.storage_policy:
            self.storage_policy.validate()
        if self.timers:
            for v1 in self.timers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_config is not None:
            result['BrowserConfig'] = self.browser_config.to_map()

        if self.browser_instance_group_id is not None:
            result['BrowserInstanceGroupId'] = self.browser_instance_group_id

        if self.cloud_browser_name is not None:
            result['CloudBrowserName'] = self.cloud_browser_name

        if self.max_amount is not None:
            result['MaxAmount'] = self.max_amount

        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy.to_map()

        result['Timers'] = []
        if self.timers is not None:
            for k1 in self.timers:
                result['Timers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserConfig') is not None:
            temp_model = main_models.ModifyBrowserInstanceGroupRequestBrowserConfig()
            self.browser_config = temp_model.from_map(m.get('BrowserConfig'))

        if m.get('BrowserInstanceGroupId') is not None:
            self.browser_instance_group_id = m.get('BrowserInstanceGroupId')

        if m.get('CloudBrowserName') is not None:
            self.cloud_browser_name = m.get('CloudBrowserName')

        if m.get('MaxAmount') is not None:
            self.max_amount = m.get('MaxAmount')

        if m.get('Network') is not None:
            temp_model = main_models.ModifyBrowserInstanceGroupRequestNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('Policy') is not None:
            temp_model = main_models.ModifyBrowserInstanceGroupRequestPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('StoragePolicy') is not None:
            temp_model = main_models.ModifyBrowserInstanceGroupRequestStoragePolicy()
            self.storage_policy = temp_model.from_map(m.get('StoragePolicy'))

        self.timers = []
        if m.get('Timers') is not None:
            for k1 in m.get('Timers'):
                temp_model = main_models.ModifyBrowserInstanceGroupRequestTimers()
                self.timers.append(temp_model.from_map(k1))

        return self

class ModifyBrowserInstanceGroupRequestTimers(DaraModel):
    def __init__(
        self,
        interval: int = None,
        timer_type: str = None,
    ):
        # The interval.
        self.interval = interval
        # The timer type.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['Interval'] = self.interval

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

class ModifyBrowserInstanceGroupRequestStoragePolicy(DaraModel):
    def __init__(
        self,
        user_profile: main_models.ModifyBrowserInstanceGroupRequestStoragePolicyUserProfile = None,
    ):
        self.user_profile = user_profile

    def validate(self):
        if self.user_profile:
            self.user_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_profile is not None:
            result['UserProfile'] = self.user_profile.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserProfile') is not None:
            temp_model = main_models.ModifyBrowserInstanceGroupRequestStoragePolicyUserProfile()
            self.user_profile = temp_model.from_map(m.get('UserProfile'))

        return self

class ModifyBrowserInstanceGroupRequestStoragePolicyUserProfile(DaraModel):
    def __init__(
        self,
        user_profile_switch: bool = None,
    ):
        self.user_profile_switch = user_profile_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_profile_switch is not None:
            result['UserProfileSwitch'] = self.user_profile_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserProfileSwitch') is not None:
            self.user_profile_switch = m.get('UserProfileSwitch')

        return self

class ModifyBrowserInstanceGroupRequestPolicy(DaraModel):
    def __init__(
        self,
        clipboard_policy: main_models.ModifyBrowserInstanceGroupRequestPolicyClipboardPolicy = None,
        disconnect_keep_session: str = None,
        disconnect_keep_session_time: int = None,
        file_manager: str = None,
        html_5file_transfer: str = None,
        no_operation_disconnect: str = None,
        no_operation_disconnect_time: int = None,
        policy_id: str = None,
        policy_version: str = None,
        video_policy: main_models.ModifyBrowserInstanceGroupRequestPolicyVideoPolicy = None,
        watermark_policy: main_models.ModifyBrowserInstanceGroupRequestPolicyWatermarkPolicy = None,
    ):
        # The clipboard policy settings.
        self.clipboard_policy = clipboard_policy
        # The data retention policy for sessions after disconnection.
        self.disconnect_keep_session = disconnect_keep_session
        # The session retention duration after disconnection.
        self.disconnect_keep_session_time = disconnect_keep_session_time
        self.file_manager = file_manager
        # The file transfer policy for the web client.
        self.html_5file_transfer = html_5file_transfer
        # The policy for disconnecting sessions after no operation.
        self.no_operation_disconnect = no_operation_disconnect
        # The idle timeout period before disconnection, in seconds.
        self.no_operation_disconnect_time = no_operation_disconnect_time
        # The policy ID.
        self.policy_id = policy_id
        # The policy version.
        self.policy_version = policy_version
        # The display policy.
        self.video_policy = video_policy
        # The watermark configuration.
        self.watermark_policy = watermark_policy

    def validate(self):
        if self.clipboard_policy:
            self.clipboard_policy.validate()
        if self.video_policy:
            self.video_policy.validate()
        if self.watermark_policy:
            self.watermark_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clipboard_policy is not None:
            result['ClipboardPolicy'] = self.clipboard_policy.to_map()

        if self.disconnect_keep_session is not None:
            result['DisconnectKeepSession'] = self.disconnect_keep_session

        if self.disconnect_keep_session_time is not None:
            result['DisconnectKeepSessionTime'] = self.disconnect_keep_session_time

        if self.file_manager is not None:
            result['FileManager'] = self.file_manager

        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer

        if self.no_operation_disconnect is not None:
            result['NoOperationDisconnect'] = self.no_operation_disconnect

        if self.no_operation_disconnect_time is not None:
            result['NoOperationDisconnectTime'] = self.no_operation_disconnect_time

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.video_policy is not None:
            result['VideoPolicy'] = self.video_policy.to_map()

        if self.watermark_policy is not None:
            result['WatermarkPolicy'] = self.watermark_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipboardPolicy') is not None:
            temp_model = main_models.ModifyBrowserInstanceGroupRequestPolicyClipboardPolicy()
            self.clipboard_policy = temp_model.from_map(m.get('ClipboardPolicy'))

        if m.get('DisconnectKeepSession') is not None:
            self.disconnect_keep_session = m.get('DisconnectKeepSession')

        if m.get('DisconnectKeepSessionTime') is not None:
            self.disconnect_keep_session_time = m.get('DisconnectKeepSessionTime')

        if m.get('FileManager') is not None:
            self.file_manager = m.get('FileManager')

        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')

        if m.get('NoOperationDisconnect') is not None:
            self.no_operation_disconnect = m.get('NoOperationDisconnect')

        if m.get('NoOperationDisconnectTime') is not None:
            self.no_operation_disconnect_time = m.get('NoOperationDisconnectTime')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('VideoPolicy') is not None:
            temp_model = main_models.ModifyBrowserInstanceGroupRequestPolicyVideoPolicy()
            self.video_policy = temp_model.from_map(m.get('VideoPolicy'))

        if m.get('WatermarkPolicy') is not None:
            temp_model = main_models.ModifyBrowserInstanceGroupRequestPolicyWatermarkPolicy()
            self.watermark_policy = temp_model.from_map(m.get('WatermarkPolicy'))

        return self

class ModifyBrowserInstanceGroupRequestPolicyWatermarkPolicy(DaraModel):
    def __init__(
        self,
        watermark_switch: str = None,
        watermark_types: List[str] = None,
    ):
        # Specifies whether to enable the watermark.
        self.watermark_switch = watermark_switch
        # The list of watermark types.
        self.watermark_types = watermark_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.watermark_switch is not None:
            result['WatermarkSwitch'] = self.watermark_switch

        if self.watermark_types is not None:
            result['WatermarkTypes'] = self.watermark_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkSwitch') is not None:
            self.watermark_switch = m.get('WatermarkSwitch')

        if m.get('WatermarkTypes') is not None:
            self.watermark_types = m.get('WatermarkTypes')

        return self

class ModifyBrowserInstanceGroupRequestPolicyVideoPolicy(DaraModel):
    def __init__(
        self,
        frame_rate: int = None,
    ):
        # The frame rate.
        self.frame_rate = frame_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')

        return self

class ModifyBrowserInstanceGroupRequestPolicyClipboardPolicy(DaraModel):
    def __init__(
        self,
        clipboard: str = None,
        clipboard_read_limit: int = None,
        clipboard_scope: str = None,
        clipboard_size_unit: str = None,
        clipboard_write_limit: int = None,
        file_clipboard: str = None,
        rich_text_clipboard: str = None,
        rich_text_clipboard_limit: int = None,
        rich_text_clipboard_read_limit: int = None,
        rich_text_clipboard_read_size_unit: str = None,
        rich_text_clipboard_size_unit: str = None,
        rich_text_clipboard_write_limit: int = None,
        rich_text_clipboard_write_size_unit: str = None,
        text_clipboard: str = None,
        text_clipboard_read_limit: int = None,
        text_clipboard_read_size_unit: str = None,
        text_clipboard_write_limit: int = None,
        text_clipboard_write_size_unit: str = None,
    ):
        # The clipboard policy.
        self.clipboard = clipboard
        # The maximum length for clipboard read operations.
        self.clipboard_read_limit = clipboard_read_limit
        # The clipboard control scope.
        self.clipboard_scope = clipboard_scope
        self.clipboard_size_unit = clipboard_size_unit
        # The maximum length for clipboard write operations.
        self.clipboard_write_limit = clipboard_write_limit
        # The file clipboard policy.
        self.file_clipboard = file_clipboard
        # The rich text clipboard policy.
        self.rich_text_clipboard = rich_text_clipboard
        self.rich_text_clipboard_limit = rich_text_clipboard_limit
        self.rich_text_clipboard_read_limit = rich_text_clipboard_read_limit
        self.rich_text_clipboard_read_size_unit = rich_text_clipboard_read_size_unit
        self.rich_text_clipboard_size_unit = rich_text_clipboard_size_unit
        self.rich_text_clipboard_write_limit = rich_text_clipboard_write_limit
        self.rich_text_clipboard_write_size_unit = rich_text_clipboard_write_size_unit
        # The text clipboard policy.
        self.text_clipboard = text_clipboard
        self.text_clipboard_read_limit = text_clipboard_read_limit
        self.text_clipboard_read_size_unit = text_clipboard_read_size_unit
        self.text_clipboard_write_limit = text_clipboard_write_limit
        self.text_clipboard_write_size_unit = text_clipboard_write_size_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard

        if self.clipboard_read_limit is not None:
            result['ClipboardReadLimit'] = self.clipboard_read_limit

        if self.clipboard_scope is not None:
            result['ClipboardScope'] = self.clipboard_scope

        if self.clipboard_size_unit is not None:
            result['ClipboardSizeUnit'] = self.clipboard_size_unit

        if self.clipboard_write_limit is not None:
            result['ClipboardWriteLimit'] = self.clipboard_write_limit

        if self.file_clipboard is not None:
            result['FileClipboard'] = self.file_clipboard

        if self.rich_text_clipboard is not None:
            result['RichTextClipboard'] = self.rich_text_clipboard

        if self.rich_text_clipboard_limit is not None:
            result['RichTextClipboardLimit'] = self.rich_text_clipboard_limit

        if self.rich_text_clipboard_read_limit is not None:
            result['RichTextClipboardReadLimit'] = self.rich_text_clipboard_read_limit

        if self.rich_text_clipboard_read_size_unit is not None:
            result['RichTextClipboardReadSizeUnit'] = self.rich_text_clipboard_read_size_unit

        if self.rich_text_clipboard_size_unit is not None:
            result['RichTextClipboardSizeUnit'] = self.rich_text_clipboard_size_unit

        if self.rich_text_clipboard_write_limit is not None:
            result['RichTextClipboardWriteLimit'] = self.rich_text_clipboard_write_limit

        if self.rich_text_clipboard_write_size_unit is not None:
            result['RichTextClipboardWriteSizeUnit'] = self.rich_text_clipboard_write_size_unit

        if self.text_clipboard is not None:
            result['TextClipboard'] = self.text_clipboard

        if self.text_clipboard_read_limit is not None:
            result['TextClipboardReadLimit'] = self.text_clipboard_read_limit

        if self.text_clipboard_read_size_unit is not None:
            result['TextClipboardReadSizeUnit'] = self.text_clipboard_read_size_unit

        if self.text_clipboard_write_limit is not None:
            result['TextClipboardWriteLimit'] = self.text_clipboard_write_limit

        if self.text_clipboard_write_size_unit is not None:
            result['TextClipboardWriteSizeUnit'] = self.text_clipboard_write_size_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')

        if m.get('ClipboardReadLimit') is not None:
            self.clipboard_read_limit = m.get('ClipboardReadLimit')

        if m.get('ClipboardScope') is not None:
            self.clipboard_scope = m.get('ClipboardScope')

        if m.get('ClipboardSizeUnit') is not None:
            self.clipboard_size_unit = m.get('ClipboardSizeUnit')

        if m.get('ClipboardWriteLimit') is not None:
            self.clipboard_write_limit = m.get('ClipboardWriteLimit')

        if m.get('FileClipboard') is not None:
            self.file_clipboard = m.get('FileClipboard')

        if m.get('RichTextClipboard') is not None:
            self.rich_text_clipboard = m.get('RichTextClipboard')

        if m.get('RichTextClipboardLimit') is not None:
            self.rich_text_clipboard_limit = m.get('RichTextClipboardLimit')

        if m.get('RichTextClipboardReadLimit') is not None:
            self.rich_text_clipboard_read_limit = m.get('RichTextClipboardReadLimit')

        if m.get('RichTextClipboardReadSizeUnit') is not None:
            self.rich_text_clipboard_read_size_unit = m.get('RichTextClipboardReadSizeUnit')

        if m.get('RichTextClipboardSizeUnit') is not None:
            self.rich_text_clipboard_size_unit = m.get('RichTextClipboardSizeUnit')

        if m.get('RichTextClipboardWriteLimit') is not None:
            self.rich_text_clipboard_write_limit = m.get('RichTextClipboardWriteLimit')

        if m.get('RichTextClipboardWriteSizeUnit') is not None:
            self.rich_text_clipboard_write_size_unit = m.get('RichTextClipboardWriteSizeUnit')

        if m.get('TextClipboard') is not None:
            self.text_clipboard = m.get('TextClipboard')

        if m.get('TextClipboardReadLimit') is not None:
            self.text_clipboard_read_limit = m.get('TextClipboardReadLimit')

        if m.get('TextClipboardReadSizeUnit') is not None:
            self.text_clipboard_read_size_unit = m.get('TextClipboardReadSizeUnit')

        if m.get('TextClipboardWriteLimit') is not None:
            self.text_clipboard_write_limit = m.get('TextClipboardWriteLimit')

        if m.get('TextClipboardWriteSizeUnit') is not None:
            self.text_clipboard_write_size_unit = m.get('TextClipboardWriteSizeUnit')

        return self

class ModifyBrowserInstanceGroupRequestNetwork(DaraModel):
    def __init__(
        self,
        access_restriction: str = None,
        remove_restricted_urlids: List[str] = None,
        restricted_urls: List[main_models.ModifyBrowserInstanceGroupRequestNetworkRestrictedURLs] = None,
        restricted_urls_file_path: str = None,
    ):
        # The access restriction type.
        self.access_restriction = access_restriction
        # The list of domain names to remove.
        self.remove_restricted_urlids = remove_restricted_urlids
        # The restricted domain name configurations.
        self.restricted_urls = restricted_urls
        self.restricted_urls_file_path = restricted_urls_file_path

    def validate(self):
        if self.restricted_urls:
            for v1 in self.restricted_urls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_restriction is not None:
            result['AccessRestriction'] = self.access_restriction

        if self.remove_restricted_urlids is not None:
            result['RemoveRestrictedURLIds'] = self.remove_restricted_urlids

        result['RestrictedURLs'] = []
        if self.restricted_urls is not None:
            for k1 in self.restricted_urls:
                result['RestrictedURLs'].append(k1.to_map() if k1 else None)

        if self.restricted_urls_file_path is not None:
            result['RestrictedURLsFilePath'] = self.restricted_urls_file_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRestriction') is not None:
            self.access_restriction = m.get('AccessRestriction')

        if m.get('RemoveRestrictedURLIds') is not None:
            self.remove_restricted_urlids = m.get('RemoveRestrictedURLIds')

        self.restricted_urls = []
        if m.get('RestrictedURLs') is not None:
            for k1 in m.get('RestrictedURLs'):
                temp_model = main_models.ModifyBrowserInstanceGroupRequestNetworkRestrictedURLs()
                self.restricted_urls.append(temp_model.from_map(k1))

        if m.get('RestrictedURLsFilePath') is not None:
            self.restricted_urls_file_path = m.get('RestrictedURLsFilePath')

        return self

class ModifyBrowserInstanceGroupRequestNetworkRestrictedURLs(DaraModel):
    def __init__(
        self,
        restricted_urlid: str = None,
        url: str = None,
    ):
        # The ID of the domain name configuration. This parameter is required only for modification.
        self.restricted_urlid = restricted_urlid
        # The domain name.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.restricted_urlid is not None:
            result['RestrictedURLId'] = self.restricted_urlid

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestrictedURLId') is not None:
            self.restricted_urlid = m.get('RestrictedURLId')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class ModifyBrowserInstanceGroupRequestBrowserConfig(DaraModel):
    def __init__(
        self,
        bookmarks: List[main_models.ModifyBrowserInstanceGroupRequestBrowserConfigBookmarks] = None,
        bookmarks_file_path: str = None,
        browser_param: str = None,
        cookies_sync: bool = None,
        homepage: str = None,
        remove_bookmarks: List[str] = None,
    ):
        # The bookmarks.
        self.bookmarks = bookmarks
        self.bookmarks_file_path = bookmarks_file_path
        # The startup parameters.
        self.browser_param = browser_param
        self.cookies_sync = cookies_sync
        # The homepage.
        self.homepage = homepage
        # The list of bookmarks to remove.
        self.remove_bookmarks = remove_bookmarks

    def validate(self):
        if self.bookmarks:
            for v1 in self.bookmarks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bookmarks'] = []
        if self.bookmarks is not None:
            for k1 in self.bookmarks:
                result['Bookmarks'].append(k1.to_map() if k1 else None)

        if self.bookmarks_file_path is not None:
            result['BookmarksFilePath'] = self.bookmarks_file_path

        if self.browser_param is not None:
            result['BrowserParam'] = self.browser_param

        if self.cookies_sync is not None:
            result['CookiesSync'] = self.cookies_sync

        if self.homepage is not None:
            result['Homepage'] = self.homepage

        if self.remove_bookmarks is not None:
            result['RemoveBookmarks'] = self.remove_bookmarks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bookmarks = []
        if m.get('Bookmarks') is not None:
            for k1 in m.get('Bookmarks'):
                temp_model = main_models.ModifyBrowserInstanceGroupRequestBrowserConfigBookmarks()
                self.bookmarks.append(temp_model.from_map(k1))

        if m.get('BookmarksFilePath') is not None:
            self.bookmarks_file_path = m.get('BookmarksFilePath')

        if m.get('BrowserParam') is not None:
            self.browser_param = m.get('BrowserParam')

        if m.get('CookiesSync') is not None:
            self.cookies_sync = m.get('CookiesSync')

        if m.get('Homepage') is not None:
            self.homepage = m.get('Homepage')

        if m.get('RemoveBookmarks') is not None:
            self.remove_bookmarks = m.get('RemoveBookmarks')

        return self

class ModifyBrowserInstanceGroupRequestBrowserConfigBookmarks(DaraModel):
    def __init__(
        self,
        bookmark_folder: str = None,
        bookmark_id: str = None,
        bookmark_name: str = None,
        bookmark_url: str = None,
    ):
        # The folder to which the bookmark belongs.
        self.bookmark_folder = bookmark_folder
        # The bookmark ID. This parameter is required only for modification.
        self.bookmark_id = bookmark_id
        # The bookmark name.
        # 
        # This parameter is required.
        self.bookmark_name = bookmark_name
        # The bookmark URL.
        # 
        # This parameter is required.
        self.bookmark_url = bookmark_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bookmark_folder is not None:
            result['BookmarkFolder'] = self.bookmark_folder

        if self.bookmark_id is not None:
            result['BookmarkId'] = self.bookmark_id

        if self.bookmark_name is not None:
            result['BookmarkName'] = self.bookmark_name

        if self.bookmark_url is not None:
            result['BookmarkURL'] = self.bookmark_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BookmarkFolder') is not None:
            self.bookmark_folder = m.get('BookmarkFolder')

        if m.get('BookmarkId') is not None:
            self.bookmark_id = m.get('BookmarkId')

        if m.get('BookmarkName') is not None:
            self.bookmark_name = m.get('BookmarkName')

        if m.get('BookmarkURL') is not None:
            self.bookmark_url = m.get('BookmarkURL')

        return self

