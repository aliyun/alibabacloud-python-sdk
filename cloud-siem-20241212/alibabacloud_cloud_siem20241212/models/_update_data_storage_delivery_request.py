# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateDataStorageDeliveryRequest(DaraModel):
    def __init__(
        self,
        auto_include_new_accounts: bool = None,
        configuration_version: int = None,
        lang: str = None,
        log_code: str = None,
        log_delivery_status: str = None,
        region_id: str = None,
        role_for: int = None,
        selected_account_ids: List[str] = None,
        sub_user_id: int = None,
        target_project: str = None,
    ):
        # 是否将后续新增且可用的纳管成员自动加入该日志类型的账号选择。true 表示开启，false 表示关闭；关闭不会移除已选择成员。省略保持原值。需同时传 LogCode、ConfigurationVersion、TargetProject，可与 SelectedAccountIds 一起更新，不可同时传 LogDeliveryStatus 或成员 SubUserId。实际投递还受多账号总开关和该日志类型投递开关控制。
        self.auto_include_new_accounts = auto_include_new_accounts
        # 本次修改所依据的投递设置版本。先调用 GetDataStorage，取 Data.DeliverySettings.ConfigurationVersion 原值传入；示例 1 仅展示格式，不能作为固定版本使用。修改总开关、账号选择、自动纳入设置或指定成员投递时必传。版本缺失或已变化时返回 OperationDenied.CentralizedDeliveryConfigChanged，应重新查询后再提交。
        self.configuration_version = configuration_version
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # This parameter is required. If this parameter is not specified, the API returns a 400 error.
        self.lang = lang
        # The log code.
        # 
        # This parameter is required.
        self.log_code = log_code
        # The log delivery status. Valid values:
        # - enable: Enables log delivery.
        # - disable: Disables log delivery.
        self.log_delivery_status = log_delivery_status
        # The region where the threat analysis data management center resides. Specify the management center based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Your assets reside outside China.
        self.region_id = region_id
        # The ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # 该日志类型的完整账号选择列表，元素为十进制 UID 字符串，必须包含 Data.DeliverySettings.DaAccountId（本账号），最多 10000 项。新增成员须在 GetDataStorage 的 Accounts 列表中且 Authorized=true。仅保留本账号时传本账号 UID，不能用空字符串或空数组代替。省略本字段保持原选择。HTTP 请求使用 array(simple) 的逗号分隔格式：SelectedAccountIds=1234567890123456,1234567890123457；单账号只传一个 UID。不使用 SelectedAccountIds.1/.2 或 JSON 数组字符串。需同时传 ConfigurationVersion、TargetProject，并省略 LogDeliveryStatus 和成员 SubUserId。
        self.selected_account_ids = selected_account_ids
        # 日志来源云账号 UID，使用十进制整数。省略或等于本账号 UID 时操作本账号投递；传成员 UID 时仅对该成员应用当前配置期望的投递状态，需同时传 LogDeliveryStatus、ConfigurationVersion、TargetProject。成员必须已在该类型选择范围中或已有投递记录。保存账号选择或自动纳入设置时应省略本字段，不可传其他成员 UID。
        self.sub_user_id = sub_user_id
        # 当前日志投递目标 SLS Project 的名称。先调用 GetDataStorage，取 Data.DeliverySettings.TargetProject 原值传入；用于校验本次修改的目标，不用于指定新的 Project。修改总开关、账号选择、自动纳入设置或指定成员投递时必传；缺失或与当前目标不同会返回 OperationDenied.CentralizedDeliveryConfigChanged。示例中的账号 UID 和地域需替换为查询结果。
        self.target_project = target_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_include_new_accounts is not None:
            result['AutoIncludeNewAccounts'] = self.auto_include_new_accounts

        if self.configuration_version is not None:
            result['ConfigurationVersion'] = self.configuration_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.log_delivery_status is not None:
            result['LogDeliveryStatus'] = self.log_delivery_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.selected_account_ids is not None:
            result['SelectedAccountIds'] = self.selected_account_ids

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.target_project is not None:
            result['TargetProject'] = self.target_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncludeNewAccounts') is not None:
            self.auto_include_new_accounts = m.get('AutoIncludeNewAccounts')

        if m.get('ConfigurationVersion') is not None:
            self.configuration_version = m.get('ConfigurationVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('LogDeliveryStatus') is not None:
            self.log_delivery_status = m.get('LogDeliveryStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('SelectedAccountIds') is not None:
            self.selected_account_ids = m.get('SelectedAccountIds')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('TargetProject') is not None:
            self.target_project = m.get('TargetProject')

        return self

