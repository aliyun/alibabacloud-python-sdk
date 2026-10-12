# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeConsoleMessagesRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        client_types: List[str] = None,
        keyword: str = None,
        message_ids: List[str] = None,
        message_level: str = None,
        message_type: str = None,
        page_num: int = None,
        page_size: int = None,
        target_ids: List[str] = None,
        target_type: str = None,
    ):
        # The business channel, which is used to limit the business to which the messages to query belong. Valid values: enterprise, standard, office, business, lincore_team, and AGENTIC_CLOUD_COMPUTER. The values are not case-sensitive. Default value: enterprise. Unrecognized channel values are also processed as enterprise.
        self.business_channel = business_channel
        # The list of client types to which operational messages apply. A maximum of 100 items can be specified. Valid values: Windows (Windows client), Mac (macOS client), Web (web client), and Hardware (hardware terminal). For Mac, macOS is also supported. The matching is not case-sensitive. If multiple types are specified, a message is matched if it applies to any of the specified types. Do not pass duplicate types. To filter by client type, provide a non-empty list. If this parameter is not specified, messages are not filtered by client type. Do not specify this parameter when querying NOTIFICATION messages.
        self.client_types = client_types
        # The search keyword, which is used to perform a fuzzy match on the message title or body. A message is returned if either the title or the body matches the keyword. If this parameter is not specified or an empty string is passed, messages are not filtered by keyword.
        self.keyword = keyword
        # The list of message IDs to query. A maximum of 100 message IDs can be specified. If multiple IDs are specified, a message is matched if its ID matches any of the specified IDs. If this parameter is not specified or an empty list is passed, messages are not filtered by message ID. If no message ID matches, an empty list is returned.
        self.message_ids = message_ids
        # The message level filter condition for notification messages. Valid values: STRONG (strong message) and WEAK (weak message). The values are not case-sensitive. If this parameter is not specified or an unrecognized value is passed, messages are not filtered by message level. Do not specify this parameter when querying OPERATIONAL messages.
        self.message_level = message_level
        # The message type. Valid values: OPERATIONAL (client operational message), WALLPAPER (desktop wallpaper text message), NOTIFICATION (message center notification), and CUSTOM_WALLPAPER (custom desktop wallpaper). The values are not case-sensitive. If this parameter is not specified or an unrecognized value is passed, messages are not filtered by message type.
        self.message_type = message_type
        # The page number of the query result. Pages start from 1. Default value: 1. If the value is less than 1, it is processed as 1.
        self.page_num = page_num
        # The number of entries per page. Valid values: 1 to 200. Default value: 200. If the value is less than 1 or greater than 200, it is processed as 200.
        self.page_size = page_size
        # The list of target IDs to match. A maximum of 100 items can be specified. To filter by target, provide a non-empty list and specify TargetType at the same time. Currently, only the first ID is used for Organization, EndUser, and AdUser. Queries for EndUser and AdUser also match messages targeted at the organization to which the user belongs and all users. Queries for Organization include messages for all convenience users and are compatible with fuzzy matching of organization IDs. Other target matching methods match based on the target ID, and the target type of the returned records is not guaranteed to be consistent with TargetType. Currently, Tag does not perform target ID filtering.
        self.target_ids = target_ids
        # The target matching method. Valid values: AllUsers (all convenience users), EndUser (specified convenience user), Organization (convenience user organization), Desktop (cloud computer), ResourceGroup (resource group), Region (region), Tag (tag), AdAllUsers (all AD users), AdUser (specified AD user), and AdOrg (AD organization). The values are not case-sensitive. If TargetIds is specified, this parameter must also be specified. The target type in the query results is not guaranteed to be consistent with this parameter. If only this parameter is specified without target IDs, no target filtering is applied. Currently, Tag does not perform target filtering.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.client_types is not None:
            result['ClientTypes'] = self.client_types

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.message_ids is not None:
            result['MessageIds'] = self.message_ids

        if self.message_level is not None:
            result['MessageLevel'] = self.message_level

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('ClientTypes') is not None:
            self.client_types = m.get('ClientTypes')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MessageIds') is not None:
            self.message_ids = m.get('MessageIds')

        if m.get('MessageLevel') is not None:
            self.message_level = m.get('MessageLevel')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

