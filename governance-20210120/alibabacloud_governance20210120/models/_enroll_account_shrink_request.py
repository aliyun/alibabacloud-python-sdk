# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class EnrollAccountShrinkRequest(DaraModel):
    def __init__(
        self,
        account_name_prefix: str = None,
        account_uid: int = None,
        baseline_id: str = None,
        baseline_items: List[main_models.EnrollAccountShrinkRequestBaselineItems] = None,
        display_name: str = None,
        folder_id: str = None,
        payer_account_uid: int = None,
        region_id: str = None,
        resell_account_type: str = None,
        tag_shrink: str = None,
    ):
        # The prefix for the account name of the member.
        # 
        # *   If the account baseline is applied to an account that is newly created, you must configure this parameter.
        # *   If the account baseline is applied to an existing account, you do not need to configure this parameter.
        self.account_name_prefix = account_name_prefix
        # The account ID.
        # 
        # *   If the account baseline is applied to an account that is newly created, you do not need to configure this parameter.
        # *   If the account baseline is applied to an existing account, you must configure this parameter.
        self.account_uid = account_uid
        # The baseline ID.
        # 
        # If this parameter is left empty, the default baseline is used.
        self.baseline_id = baseline_id
        # The array that contains baseline items.
        # 
        # If this parameter is specified, the configurations of the baseline items are merged with the baseline applied to the specified account. The configurations of the same baseline items are subject to the configurations of this parameter. We recommend that you leave this parameter empty and configure the `BaselineId` parameter to specify an account baseline and apply the configurations of the account baseline to the account.
        self.baseline_items = baseline_items
        # The display name of the account.
        # 
        # *   If the account baseline is applied to an account that is newly created, you must configure this parameter.
        # *   If the account baseline is applied to an existing account, you do not need to configure this parameter.
        self.display_name = display_name
        # The ID of the parent folder.
        # 
        # *   If the account baseline is applied to an account that is newly created, you need to specify a parent folder. If you do not configure this parameter, the account is created in the Root folder.
        # *   If the account baseline is applied to an existing account, you do not need to configure this parameter.
        self.folder_id = folder_id
        # The ID of the billing account.
        # 
        # *   If the account baseline is applied to an account that is newly created, you need to specify a billing account. If you do not configure this parameter, the self-pay settlement method is used for the account.
        # *   If the account baseline is applied to an existing account, you do not need to configure this parameter.
        self.payer_account_uid = payer_account_uid
        # The region ID.
        self.region_id = region_id
        # The identity type of the member. Valid values:
        # 
        # *   resell (default): The member is an account for a reseller. A relationship is automatically established between the member and the reseller. The management account of the resource directory must be used as the billing account of the member.
        # *   non_resell: The member is not an account for a reseller. The member is an account that is not associated with a reseller. You can directly use the account to purchase Alibaba Cloud resources. The member is used as its own billing account.
        # 
        # > This parameter is available only for resellers at the international site (alibabacloud.com).
        self.resell_account_type = resell_account_type
        # The tags. You can specify up to 20 tags.
        self.tag_shrink = tag_shrink

    def validate(self):
        if self.baseline_items:
            for v1 in self.baseline_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix

        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid

        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k1 in self.baseline_items:
                result['BaselineItems'].append(k1.to_map() if k1 else None)

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resell_account_type is not None:
            result['ResellAccountType'] = self.resell_account_type

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNamePrefix') is not None:
            self.account_name_prefix = m.get('AccountNamePrefix')

        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')

        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k1 in m.get('BaselineItems'):
                temp_model = main_models.EnrollAccountShrinkRequestBaselineItems()
                self.baseline_items.append(temp_model.from_map(k1))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellAccountType') is not None:
            self.resell_account_type = m.get('ResellAccountType')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

class EnrollAccountShrinkRequestBaselineItems(DaraModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        skip: bool = None,
        version: str = None,
    ):
        # The configurations of the baseline item.
        self.config = config
        # The name of the baseline item.
        self.name = name
        # Whether to skip the baseline item. Valid values:
        # 
        # *   false: The baseline item is not skipped.
        # *   true: The baseline item is skipped.
        self.skip = skip
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.name is not None:
            result['Name'] = self.name

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

