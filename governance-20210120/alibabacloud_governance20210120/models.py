# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class BatchEnrollAccountsRequestAccounts(TeaModel):
    def __init__(
        self,
        account_uid: int = None,
    ):
        # The account ID. This parameter is required.
        self.account_uid = account_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        return self


class BatchEnrollAccountsRequestBaselineItems(TeaModel):
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
        # Specifies whether to skip the baseline item. Valid values:
        # 
        # *   false
        # *   true
        self.skip = skip
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class BatchEnrollAccountsRequest(TeaModel):
    def __init__(
        self,
        accounts: List[BatchEnrollAccountsRequestAccounts] = None,
        baseline_id: str = None,
        baseline_items: List[BatchEnrollAccountsRequestBaselineItems] = None,
        region_id: str = None,
    ):
        # The resource accounts.
        self.accounts = accounts
        # The baseline ID.
        # 
        # If this parameter is left empty, the default baseline is used.
        self.baseline_id = baseline_id
        # The baseline items.
        # 
        # If this parameter is specified, the configurations of the baseline items are merged with the baseline applied to the specified account. The configurations of the same baseline items are subject to the configurations of this parameter. We recommend that you leave this parameter empty and configure the `BaselineId` parameter to specify an account baseline and apply the configurations of the account baseline to the account.
        self.baseline_items = baseline_items
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = BatchEnrollAccountsRequestAccounts()
                self.accounts.append(temp_model.from_map(k))
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = BatchEnrollAccountsRequestBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BatchEnrollAccountsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchEnrollAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchEnrollAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchEnrollAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountFactoryBaselineRequestBaselineItems(TeaModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        version: str = None,
    ):
        # The configurations of the baseline item. The value of this parameter is a JSON string.
        self.config = config
        # The name of the baseline item.
        self.name = name
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateAccountFactoryBaselineRequest(TeaModel):
    def __init__(
        self,
        baseline_items: List[CreateAccountFactoryBaselineRequestBaselineItems] = None,
        baseline_name: str = None,
        description: str = None,
        region_id: str = None,
    ):
        # An array that contains the baseline items.
        # 
        # You can call the [ListAccountFactoryBaselineItems](~~ListAccountFactoryBaselineItems~~) operation to query a list of baseline items supported by the account factory in Cloud Governance Center.
        self.baseline_items = baseline_items
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The description of the baseline.
        self.description = description
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = CreateAccountFactoryBaselineRequestBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateAccountFactoryBaselineResponseBody(TeaModel):
    def __init__(
        self,
        baseline_id: str = None,
        request_id: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccountFactoryBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccountFactoryBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccountFactoryBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountFactoryBaselineRequest(TeaModel):
    def __init__(
        self,
        baseline_id: str = None,
        region_id: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAccountFactoryBaselineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAccountFactoryBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccountFactoryBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccountFactoryBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnrollAccountRequestBaselineItems(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class EnrollAccountRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class EnrollAccountRequest(TeaModel):
    def __init__(
        self,
        account_name_prefix: str = None,
        account_uid: int = None,
        baseline_id: str = None,
        baseline_items: List[EnrollAccountRequestBaselineItems] = None,
        display_name: str = None,
        folder_id: str = None,
        payer_account_uid: int = None,
        region_id: str = None,
        resell_account_type: str = None,
        tag: List[EnrollAccountRequestTag] = None,
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
        self.tag = tag

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
            for k in m.get('BaselineItems'):
                temp_model = EnrollAccountRequestBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = EnrollAccountRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class EnrollAccountShrinkRequestBaselineItems(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class EnrollAccountShrinkRequest(TeaModel):
    def __init__(
        self,
        account_name_prefix: str = None,
        account_uid: int = None,
        baseline_id: str = None,
        baseline_items: List[EnrollAccountShrinkRequestBaselineItems] = None,
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
            for k in self.baseline_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
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
            for k in m.get('BaselineItems'):
                temp_model = EnrollAccountShrinkRequestBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
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


class EnrollAccountResponseBody(TeaModel):
    def __init__(
        self,
        account_uid: int = None,
        request_id: str = None,
    ):
        # The account ID.
        self.account_uid = account_uid
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnrollAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnrollAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnrollAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountFactoryBaselineRequest(TeaModel):
    def __init__(
        self,
        baseline_id: str = None,
        region_id: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAccountFactoryBaselineResponseBodyBaselineItems(TeaModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        version: str = None,
    ):
        # The configuration of the baseline item.
        # 
        # The value is a JSON string.
        self.config = config
        # The name of the baseline item.
        self.name = name
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAccountFactoryBaselineResponseBody(TeaModel):
    def __init__(
        self,
        baseline_id: str = None,
        baseline_items: List[GetAccountFactoryBaselineResponseBodyBaselineItems] = None,
        baseline_name: str = None,
        create_time: str = None,
        description: str = None,
        request_id: str = None,
        type: str = None,
        update_time: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The baseline items.
        self.baseline_items = baseline_items
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The time when the baseline was created.
        self.create_time = create_time
        # The description of the baseline.
        self.description = description
        # The request ID.
        self.request_id = request_id
        # The type of the baseline. Valid values:
        # 
        # *   System: default baseline.
        # *   Custom: custom baseline.
        self.type = type
        # The time when the baseline was updated.
        self.update_time = update_time

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = GetAccountFactoryBaselineResponseBodyBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetAccountFactoryBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountFactoryBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccountFactoryBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnrolledAccountRequest(TeaModel):
    def __init__(
        self,
        account_uid: int = None,
        region_id: str = None,
    ):
        # The account ID.
        # 
        # This parameter is required.
        self.account_uid = account_uid
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetEnrolledAccountResponseBodyBaselineItems(TeaModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        skip: bool = None,
        version: str = None,
    ):
        # The configuration of the baseline item.
        self.config = config
        # The name of the baseline item.
        self.name = name
        # Indicates whether baseline item is skipped. Valid values:
        # 
        # *   false
        # *   true
        self.skip = skip
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetEnrolledAccountResponseBodyErrorInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        recommend: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The recommended solution.
        self.recommend = recommend
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.recommend is not None:
            result['Recommend'] = self.recommend
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Recommend') is not None:
            self.recommend = m.get('Recommend')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEnrolledAccountResponseBodyInputsBaselineItems(TeaModel):
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
        # Indicates whether baseline item is skipped. Valid values:
        # 
        # *   false
        # *   true
        self.skip = skip
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetEnrolledAccountResponseBodyInputsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetEnrolledAccountResponseBodyInputs(TeaModel):
    def __init__(
        self,
        account_name_prefix: str = None,
        account_uid: int = None,
        baseline_items: List[GetEnrolledAccountResponseBodyInputsBaselineItems] = None,
        display_name: str = None,
        folder_id: str = None,
        payer_account_uid: int = None,
        tag: List[GetEnrolledAccountResponseBodyInputsTag] = None,
    ):
        # The prefix of the account name.
        self.account_name_prefix = account_name_prefix
        # The account ID.
        self.account_uid = account_uid
        # The baseline items.
        self.baseline_items = baseline_items
        # The display name of the account.
        self.display_name = display_name
        # The ID of the parent folder.
        self.folder_id = folder_id
        # The ID of the settlement account.
        self.payer_account_uid = payer_account_uid
        # The tag.
        self.tag = tag

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNamePrefix') is not None:
            self.account_name_prefix = m.get('AccountNamePrefix')
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = GetEnrolledAccountResponseBodyInputsBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetEnrolledAccountResponseBodyInputsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetEnrolledAccountResponseBodyProgress(TeaModel):
    def __init__(
        self,
        name: str = None,
        status: str = None,
    ):
        # The name of the baseline item.
        self.name = name
        # The status of applying the baseline to the account. Valid values:
        # 
        # *   Pending: The baseline is pending to be applied to the account.
        # *   Running: The baseline is being applied to the account.
        # *   Finished: : The baseline is applied to the account.
        # *   Failed: : The baseline fails to be applied to the account.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetEnrolledAccountResponseBody(TeaModel):
    def __init__(
        self,
        account_uid: int = None,
        baseline_id: str = None,
        baseline_items: List[GetEnrolledAccountResponseBodyBaselineItems] = None,
        create_time: str = None,
        display_name: str = None,
        error_info: GetEnrolledAccountResponseBodyErrorInfo = None,
        folder_id: str = None,
        initialized: bool = None,
        inputs: GetEnrolledAccountResponseBodyInputs = None,
        master_account_uid: int = None,
        payer_account_uid: int = None,
        progress: List[GetEnrolledAccountResponseBodyProgress] = None,
        request_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The account ID.
        self.account_uid = account_uid
        # The ID of the baseline that is implemented.
        self.baseline_id = baseline_id
        # The array that contains baseline items.
        self.baseline_items = baseline_items
        # The time when the account was created.
        self.create_time = create_time
        # The display name of the account.
        self.display_name = display_name
        # The error message.
        # 
        # >  This parameter is returned if the value of `Status` is `Failed` or `ScheduleFailed`.
        self.error_info = error_info
        # The ID of the parent folder.
        self.folder_id = folder_id
        # Indicates whether the initialization is complete. Valid values:
        # 
        # *   false
        # *   true
        self.initialized = initialized
        # Input parameters used to create an account.
        self.inputs = inputs
        # The ID of the management account of the resource directory to which the account belongs.
        self.master_account_uid = master_account_uid
        # The ID of the settlement account.
        self.payer_account_uid = payer_account_uid
        # The progress of the applying the baseline to the account.
        self.progress = progress
        # The request ID.
        self.request_id = request_id
        # The status of the account. Valid values:
        # 
        # *   Pending: The account is pending to be created.
        # *   Running: The account is being created.
        # *   Finished: The account is created.
        # *   Failed: The account fails to be created.
        # *   Scheduling: The account is being scheduled.
        # *   ScheduleFailed: The account fails to be scheduled.
        self.status = status
        # The update time.
        self.update_time = update_time

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()
        if self.error_info:
            self.error_info.validate()
        if self.inputs:
            self.inputs.validate()
        if self.progress:
            for k in self.progress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info.to_map()
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.initialized is not None:
            result['Initialized'] = self.initialized
        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()
        if self.master_account_uid is not None:
            result['MasterAccountUid'] = self.master_account_uid
        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid
        result['Progress'] = []
        if self.progress is not None:
            for k in self.progress:
                result['Progress'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = GetEnrolledAccountResponseBodyBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ErrorInfo') is not None:
            temp_model = GetEnrolledAccountResponseBodyErrorInfo()
            self.error_info = temp_model.from_map(m['ErrorInfo'])
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('Initialized') is not None:
            self.initialized = m.get('Initialized')
        if m.get('Inputs') is not None:
            temp_model = GetEnrolledAccountResponseBodyInputs()
            self.inputs = temp_model.from_map(m['Inputs'])
        if m.get('MasterAccountUid') is not None:
            self.master_account_uid = m.get('MasterAccountUid')
        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')
        self.progress = []
        if m.get('Progress') is not None:
            for k in m.get('Progress'):
                temp_model = GetEnrolledAccountResponseBodyProgress()
                self.progress.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetEnrolledAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEnrolledAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEnrolledAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountFactoryBaselineItemsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        names: List[str] = None,
        next_token: str = None,
        region_id: str = None,
        type: str = None,
        versions: List[str] = None,
    ):
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The names of the baseline items.
        self.names = names
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The type of the baseline items.
        self.type = type
        # The versions of the baseline items.
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.names is not None:
            result['Names'] = self.names
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.versions is not None:
            result['Versions'] = self.versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Versions') is not None:
            self.versions = m.get('Versions')
        return self


class ListAccountFactoryBaselineItemsResponseBodyBaselineItemsDependsOn(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        # The name of the baseline item.
        self.name = name
        # The type of the baseline item.
        self.type = type
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAccountFactoryBaselineItemsResponseBodyBaselineItems(TeaModel):
    def __init__(
        self,
        depends_on: List[ListAccountFactoryBaselineItemsResponseBodyBaselineItemsDependsOn] = None,
        description: str = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        # The dependency of the baseline item.
        self.depends_on = depends_on
        # The description of the baseline item.
        self.description = description
        # The name of the baseline item.
        self.name = name
        # The type of the baseline item.
        self.type = type
        # The version of the baseline item.
        self.version = version

    def validate(self):
        if self.depends_on:
            for k in self.depends_on:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DependsOn'] = []
        if self.depends_on is not None:
            for k in self.depends_on:
                result['DependsOn'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.depends_on = []
        if m.get('DependsOn') is not None:
            for k in m.get('DependsOn'):
                temp_model = ListAccountFactoryBaselineItemsResponseBodyBaselineItemsDependsOn()
                self.depends_on.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAccountFactoryBaselineItemsResponseBody(TeaModel):
    def __init__(
        self,
        baseline_items: List[ListAccountFactoryBaselineItemsResponseBodyBaselineItems] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The baseline items.
        self.baseline_items = baseline_items
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = ListAccountFactoryBaselineItemsResponseBodyBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccountFactoryBaselineItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountFactoryBaselineItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccountFactoryBaselineItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountFactoryBaselinesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAccountFactoryBaselinesResponseBodyBaselines(TeaModel):
    def __init__(
        self,
        baseline_id: str = None,
        baseline_name: str = None,
        create_time: str = None,
        description: str = None,
        type: str = None,
        update_time: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The time at which the baseline was created.
        self.create_time = create_time
        # The description of the baseline.
        self.description = description
        # The type of the baseline. Valid values:
        # 
        # *   System: default baseline.
        # *   Custom: custom baseline.
        self.type = type
        # The time when the baseline was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListAccountFactoryBaselinesResponseBody(TeaModel):
    def __init__(
        self,
        baselines: List[ListAccountFactoryBaselinesResponseBodyBaselines] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The baselines.
        self.baselines = baselines
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.baselines:
            for k in self.baselines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Baselines'] = []
        if self.baselines is not None:
            for k in self.baselines:
                result['Baselines'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baselines = []
        if m.get('Baselines') is not None:
            for k in m.get('Baselines'):
                temp_model = ListAccountFactoryBaselinesResponseBodyBaselines()
                self.baselines.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccountFactoryBaselinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountFactoryBaselinesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccountFactoryBaselinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnrolledAccountsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        # 
        # You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEnrolledAccountsResponseBodyEnrolledAccounts(TeaModel):
    def __init__(
        self,
        account_uid: int = None,
        baseline_id: str = None,
        create_time: str = None,
        display_name: str = None,
        folder_id: str = None,
        payer_account_uid: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # The account ID.
        self.account_uid = account_uid
        # The ID of the baseline that is implemented.
        self.baseline_id = baseline_id
        # The creation time.
        self.create_time = create_time
        # The display name of the account.
        self.display_name = display_name
        # The ID of the parent folder.
        self.folder_id = folder_id
        # The ID of the settlement account.
        self.payer_account_uid = payer_account_uid
        # The creation status. Valid values:
        # 
        # *   Pending: The account is pending to be created.
        # *   Running: The account is being created.
        # *   Finished: The account is created.
        # *   Failed: The account fails to be created.
        # *   Scheduling: The account is being scheduled.
        # *   ScheduleFailed: The account fails to be scheduled.
        self.status = status
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id
        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')
        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListEnrolledAccountsResponseBody(TeaModel):
    def __init__(
        self,
        enrolled_accounts: List[ListEnrolledAccountsResponseBodyEnrolledAccounts] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The enrolled accounts.
        self.enrolled_accounts = enrolled_accounts
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.enrolled_accounts:
            for k in self.enrolled_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EnrolledAccounts'] = []
        if self.enrolled_accounts is not None:
            for k in self.enrolled_accounts:
                result['EnrolledAccounts'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.enrolled_accounts = []
        if m.get('EnrolledAccounts') is not None:
            for k in m.get('EnrolledAccounts'):
                temp_model = ListEnrolledAccountsResponseBodyEnrolledAccounts()
                self.enrolled_accounts.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEnrolledAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnrolledAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEnrolledAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEvaluationMetadataRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        lens_code: str = None,
        region_id: str = None,
    ):
        # The language. The information is returned in the specified language. Valid values:
        # 
        # *   en: English
        # *   zh: Chinese
        self.language = language
        self.lens_code = lens_code
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.lens_code is not None:
            result['LensCode'] = self.lens_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LensCode') is not None:
            self.lens_code = m.get('LensCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActionsGuidance(TeaModel):
    def __init__(
        self,
        button_name: str = None,
        button_ref: str = None,
        content: str = None,
        title: str = None,
    ):
        # The display name of the fixing button.
        self.button_name = button_name
        # The navigation URL of the fixing button.
        self.button_ref = button_ref
        # The fixing procedure.
        self.content = content
        # The title of the fixing procedure.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.button_name is not None:
            result['ButtonName'] = self.button_name
        if self.button_ref is not None:
            result['ButtonRef'] = self.button_ref
        if self.content is not None:
            result['Content'] = self.content
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ButtonName') is not None:
            self.button_name = m.get('ButtonName')
        if m.get('ButtonRef') is not None:
            self.button_ref = m.get('ButtonRef')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActions(TeaModel):
    def __init__(
        self,
        classification: str = None,
        cost_description: str = None,
        description: str = None,
        guidance: List[ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActionsGuidance] = None,
        notice: str = None,
        suggestion: str = None,
    ):
        # The fixing method.
        # 
        # >  This parameter is returned only if the value of `RemediationType` is `Analysis`.
        self.classification = classification
        # The fixing cost.
        self.cost_description = cost_description
        # The description of the fixing item.
        # 
        # >  This parameter is returned only if the value of `RemediationType` is `Analysis`.
        self.description = description
        # The content of the fixing items.
        self.guidance = guidance
        # The usage notes of the fixing item.
        self.notice = notice
        # The fixing suggestion.
        # 
        # >  This parameter is returned only if the value of `RemediationType` is `Analysis`.
        self.suggestion = suggestion

    def validate(self):
        if self.guidance:
            for k in self.guidance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.cost_description is not None:
            result['CostDescription'] = self.cost_description
        if self.description is not None:
            result['Description'] = self.description
        result['Guidance'] = []
        if self.guidance is not None:
            for k in self.guidance:
                result['Guidance'].append(k.to_map() if k else None)
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('CostDescription') is not None:
            self.cost_description = m.get('CostDescription')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.guidance = []
        if m.get('Guidance') is not None:
            for k in m.get('Guidance'):
                temp_model = ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActionsGuidance()
                self.guidance.append(temp_model.from_map(k))
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediation(TeaModel):
    def __init__(
        self,
        actions: List[ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActions] = None,
        remediation_type: str = None,
    ):
        # The fixing operations.
        self.actions = actions
        # The type of the fixing method. Valid values:
        # 
        # *   Manual: manual fixing
        # *   QuickFix: quick fixing
        # *   Analysis: auxiliary decision-making
        self.remediation_type = remediation_type

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediationActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')
        return self


class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadata(TeaModel):
    def __init__(
        self,
        remediation: List[ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediation] = None,
    ):
        # The fixing items.
        self.remediation = remediation

    def validate(self):
        if self.remediation:
            for k in self.remediation:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Remediation'] = []
        if self.remediation is not None:
            for k in self.remediation:
                result['Remediation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remediation = []
        if m.get('Remediation') is not None:
            for k in m.get('Remediation'):
                temp_model = ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadataRemediation()
                self.remediation.append(temp_model.from_map(k))
        return self


class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadataResourcePropertyMetadata(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        property_name: str = None,
        property_type: str = None,
    ):
        # The display name of the resource property.
        self.display_name = display_name
        # The name of the resource property.
        self.property_name = property_name
        # The type of the resource property.
        self.property_type = property_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_type is not None:
            result['PropertyType'] = self.property_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyType') is not None:
            self.property_type = m.get('PropertyType')
        return self


class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadata(TeaModel):
    def __init__(
        self,
        resource_property_metadata: List[ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadataResourcePropertyMetadata] = None,
    ):
        # The metadata of the resource properties.
        self.resource_property_metadata = resource_property_metadata

    def validate(self):
        if self.resource_property_metadata:
            for k in self.resource_property_metadata:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourcePropertyMetadata'] = []
        if self.resource_property_metadata is not None:
            for k in self.resource_property_metadata:
                result['ResourcePropertyMetadata'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_property_metadata = []
        if m.get('ResourcePropertyMetadata') is not None:
            for k in m.get('ResourcePropertyMetadata'):
                temp_model = ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadataResourcePropertyMetadata()
                self.resource_property_metadata.append(temp_model.from_map(k))
        return self


class ListEvaluationMetadataResponseBodyEvaluationMetadataMetadata(TeaModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        display_name: str = None,
        id: str = None,
        recommendation_level: str = None,
        remediation_metadata: ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadata = None,
        resource_metadata: ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadata = None,
        scope: str = None,
        stage: str = None,
    ):
        # The category of the check item.
        self.category = category
        # The description of the check item.
        self.description = description
        # The display name of the check item.
        self.display_name = display_name
        # The ID of the metadata.
        self.id = id
        # The governance level of the check item.
        self.recommendation_level = recommendation_level
        # The metadata of the fixing task.
        self.remediation_metadata = remediation_metadata
        # The metadata of the checked resources.
        self.resource_metadata = resource_metadata
        # The scope of the check item. Valid values:
        # 
        # *   Account: the check item in a single-account governance maturity check
        # *   ResourceDirectory: the check item in a multi-account governance maturity check
        self.scope = scope
        # The status of the check item. Valid values:
        # 
        # *   Released: The check item is released.
        # *   Beta: The check item is pre-released.
        self.stage = stage

    def validate(self):
        if self.remediation_metadata:
            self.remediation_metadata.validate()
        if self.resource_metadata:
            self.resource_metadata.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.recommendation_level is not None:
            result['RecommendationLevel'] = self.recommendation_level
        if self.remediation_metadata is not None:
            result['RemediationMetadata'] = self.remediation_metadata.to_map()
        if self.resource_metadata is not None:
            result['ResourceMetadata'] = self.resource_metadata.to_map()
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.stage is not None:
            result['Stage'] = self.stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RecommendationLevel') is not None:
            self.recommendation_level = m.get('RecommendationLevel')
        if m.get('RemediationMetadata') is not None:
            temp_model = ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataRemediationMetadata()
            self.remediation_metadata = temp_model.from_map(m['RemediationMetadata'])
        if m.get('ResourceMetadata') is not None:
            temp_model = ListEvaluationMetadataResponseBodyEvaluationMetadataMetadataResourceMetadata()
            self.resource_metadata = temp_model.from_map(m['ResourceMetadata'])
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Stage') is not None:
            self.stage = m.get('Stage')
        return self


class ListEvaluationMetadataResponseBodyEvaluationMetadata(TeaModel):
    def __init__(
        self,
        metadata: List[ListEvaluationMetadataResponseBodyEvaluationMetadataMetadata] = None,
        type: str = None,
    ):
        # The metadata objects of a specific metadata type.
        self.metadata = metadata
        # The type of the metadata. Valid values:
        # 
        # *   Metric: the check item
        self.type = type

    def validate(self):
        if self.metadata:
            for k in self.metadata:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metadata'] = []
        if self.metadata is not None:
            for k in self.metadata:
                result['Metadata'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metadata = []
        if m.get('Metadata') is not None:
            for k in m.get('Metadata'):
                temp_model = ListEvaluationMetadataResponseBodyEvaluationMetadataMetadata()
                self.metadata.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListEvaluationMetadataResponseBody(TeaModel):
    def __init__(
        self,
        evaluation_metadata: List[ListEvaluationMetadataResponseBodyEvaluationMetadata] = None,
        request_id: str = None,
    ):
        # The metadata of a governance maturity check.
        self.evaluation_metadata = evaluation_metadata
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.evaluation_metadata:
            for k in self.evaluation_metadata:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EvaluationMetadata'] = []
        if self.evaluation_metadata is not None:
            for k in self.evaluation_metadata:
                result['EvaluationMetadata'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_metadata = []
        if m.get('EvaluationMetadata') is not None:
            for k in m.get('EvaluationMetadata'):
                temp_model = ListEvaluationMetadataResponseBodyEvaluationMetadata()
                self.evaluation_metadata.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEvaluationMetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEvaluationMetadataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEvaluationMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEvaluationMetricDetailsRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        scope: str = None,
        snapshot_id: str = None,
    ):
        # The Alibaba Cloud account ID of the member. This parameter takes effect only when a multi-account governance maturity check is performed.
        self.account_id = account_id
        # The ID of the check item.
        # 
        # You can call the [ListEvaluationMetadata](https://help.aliyun.com/document_detail/2841889.html) operation to query the ID of the check item.
        self.id = id
        # The maximum number of entries to return for a single request. Default value: 5.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        self.scope = scope
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.id is not None:
            result['Id'] = self.id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ListEvaluationMetricDetailsResponseBodyResourcesResourceProperties(TeaModel):
    def __init__(
        self,
        property_name: str = None,
        property_value: str = None,
    ):
        # The name of the resource attribute.
        self.property_name = property_name
        # The value of the resource attribute.
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        return self


class ListEvaluationMetricDetailsResponseBodyResources(TeaModel):
    def __init__(
        self,
        compliance_type: str = None,
        region_id: str = None,
        resource_classification: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_owner_id: int = None,
        resource_properties: List[ListEvaluationMetricDetailsResponseBodyResourcesResourceProperties] = None,
        resource_type: str = None,
    ):
        # The compliance status of the resource. Valid values:
        # 
        # *   NonCompliant: non-compliant.
        # *   Excluded: ignored.
        # *   PendingExclusion: to be ignored.
        # *   PendingInclusion: to be unignored.
        self.compliance_type = compliance_type
        # The region ID of the resource.
        self.region_id = region_id
        # The check results further analyzed by auxiliary decision-making.
        # 
        # >  This parameter is returned only when the check item supports the auxiliary decision-making feature.
        self.resource_classification = resource_classification
        # The ID of the resource.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The ID of the Alibaba Cloud account that owns the resource.
        self.resource_owner_id = resource_owner_id
        # The attributes of the resource.
        self.resource_properties = resource_properties
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        if self.resource_properties:
            for k in self.resource_properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_classification is not None:
            result['ResourceClassification'] = self.resource_classification
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['ResourceProperties'] = []
        if self.resource_properties is not None:
            for k in self.resource_properties:
                result['ResourceProperties'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceClassification') is not None:
            self.resource_classification = m.get('ResourceClassification')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.resource_properties = []
        if m.get('ResourceProperties') is not None:
            for k in m.get('ResourceProperties'):
                temp_model = ListEvaluationMetricDetailsResponseBodyResourcesResourceProperties()
                self.resource_properties.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListEvaluationMetricDetailsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resources: List[ListEvaluationMetricDetailsResponseBodyResources] = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The details of the non-compliant resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListEvaluationMetricDetailsResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListEvaluationMetricDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEvaluationMetricDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEvaluationMetricDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEvaluationResultsRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The key of the filter condition. Valid values:
        # 
        # *   ResourceId: the resource ID.
        # *   ResourceName: the name of the resource.
        # *   ResourceType: the resource type.
        self.key = key
        # The list of filter condition values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListEvaluationResultsRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        filters: List[ListEvaluationResultsRequestFilters] = None,
        lens_code: str = None,
        region_id: str = None,
        scope: str = None,
        snapshot_id: str = None,
    ):
        # The Alibaba Cloud account ID of the member. This parameter takes effect only when a multi-account governance maturity check is performed.
        self.account_id = account_id
        # The filter conditions.
        self.filters = filters
        self.lens_code = lens_code
        # The region ID.
        self.region_id = region_id
        self.scope = scope
        self.snapshot_id = snapshot_id

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.lens_code is not None:
            result['LensCode'] = self.lens_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListEvaluationResultsRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('LensCode') is not None:
            self.lens_code = m.get('LensCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ListEvaluationResultsResponseBodyResultsMetricResultsAccountSummary(TeaModel):
    def __init__(
        self,
        non_compliant: int = None,
    ):
        self.non_compliant = non_compliant

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_compliant is not None:
            result['NonCompliant'] = self.non_compliant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonCompliant') is not None:
            self.non_compliant = m.get('NonCompliant')
        return self


class ListEvaluationResultsResponseBodyResultsMetricResultsErrorInfo(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListEvaluationResultsResponseBodyResultsMetricResultsResourcesSummary(TeaModel):
    def __init__(
        self,
        non_compliant: int = None,
    ):
        # The number of non-compliant resources.
        self.non_compliant = non_compliant

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_compliant is not None:
            result['NonCompliant'] = self.non_compliant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonCompliant') is not None:
            self.non_compliant = m.get('NonCompliant')
        return self


class ListEvaluationResultsResponseBodyResultsMetricResults(TeaModel):
    def __init__(
        self,
        account_summary: ListEvaluationResultsResponseBodyResultsMetricResultsAccountSummary = None,
        error_info: ListEvaluationResultsResponseBodyResultsMetricResultsErrorInfo = None,
        evaluation_time: str = None,
        id: str = None,
        resources_summary: ListEvaluationResultsResponseBodyResultsMetricResultsResourcesSummary = None,
        result: float = None,
        risk: str = None,
        status: str = None,
    ):
        self.account_summary = account_summary
        # The error information.
        # 
        # >  This parameter is returned only if the value of `Status` is `Failed`.
        self.error_info = error_info
        # The end time of the check item. The time is displayed in UTC.
        self.evaluation_time = evaluation_time
        # The ID of the check item.
        self.id = id
        # The checked resources.
        self.resources_summary = resources_summary
        # The rate of the non-compliant resources.
        self.result = result
        # The risk level. Valid values:
        # 
        # *   Error: high risk
        # *   Warning: medium risk
        # *   None: no risk
        self.risk = risk
        # The status of the check item. Valid values:
        # 
        # *   Running: The check is in progress.
        # *   Finished: The check is complete.
        # *   failed: The check fails.
        self.status = status

    def validate(self):
        if self.account_summary:
            self.account_summary.validate()
        if self.error_info:
            self.error_info.validate()
        if self.resources_summary:
            self.resources_summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_summary is not None:
            result['AccountSummary'] = self.account_summary.to_map()
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info.to_map()
        if self.evaluation_time is not None:
            result['EvaluationTime'] = self.evaluation_time
        if self.id is not None:
            result['Id'] = self.id
        if self.resources_summary is not None:
            result['ResourcesSummary'] = self.resources_summary.to_map()
        if self.result is not None:
            result['Result'] = self.result
        if self.risk is not None:
            result['Risk'] = self.risk
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountSummary') is not None:
            temp_model = ListEvaluationResultsResponseBodyResultsMetricResultsAccountSummary()
            self.account_summary = temp_model.from_map(m['AccountSummary'])
        if m.get('ErrorInfo') is not None:
            temp_model = ListEvaluationResultsResponseBodyResultsMetricResultsErrorInfo()
            self.error_info = temp_model.from_map(m['ErrorInfo'])
        if m.get('EvaluationTime') is not None:
            self.evaluation_time = m.get('EvaluationTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ResourcesSummary') is not None:
            temp_model = ListEvaluationResultsResponseBodyResultsMetricResultsResourcesSummary()
            self.resources_summary = temp_model.from_map(m['ResourcesSummary'])
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Risk') is not None:
            self.risk = m.get('Risk')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListEvaluationResultsResponseBodyResults(TeaModel):
    def __init__(
        self,
        evaluation_time: str = None,
        metric_results: List[ListEvaluationResultsResponseBodyResultsMetricResults] = None,
        status: str = None,
        total_score: float = None,
    ):
        # The end time of the overall check. The time is displayed in UTC.
        self.evaluation_time = evaluation_time
        # The check results.
        self.metric_results = metric_results
        # The status of the overall check. Valid values:
        # 
        # *   Running: The check is in progress.
        # *   Finished: The check is complete.
        # *   failed: The check fails.
        self.status = status
        # The overall score.
        self.total_score = total_score

    def validate(self):
        if self.metric_results:
            for k in self.metric_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_time is not None:
            result['EvaluationTime'] = self.evaluation_time
        result['MetricResults'] = []
        if self.metric_results is not None:
            for k in self.metric_results:
                result['MetricResults'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.total_score is not None:
            result['TotalScore'] = self.total_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationTime') is not None:
            self.evaluation_time = m.get('EvaluationTime')
        self.metric_results = []
        if m.get('MetricResults') is not None:
            for k in m.get('MetricResults'):
                temp_model = ListEvaluationResultsResponseBodyResultsMetricResults()
                self.metric_results.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')
        return self


class ListEvaluationResultsResponseBody(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        request_id: str = None,
        results: ListEvaluationResultsResponseBodyResults = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The request ID.
        self.request_id = request_id
        # The check results, including the status of the overall check and the results of check items.
        self.results = results

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            temp_model = ListEvaluationResultsResponseBodyResults()
            self.results = temp_model.from_map(m['Results'])
        return self


class ListEvaluationResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEvaluationResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEvaluationResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEvaluationScoreHistoryRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        end_date: str = None,
        region_id: str = None,
        start_date: str = None,
    ):
        # The Alibaba Cloud account ID of the member. This parameter takes effect only when a multi-account governance maturity check is performed.
        self.account_id = account_id
        # The end of the time range to query. Specify the time in the YYYY-MM-DD format.
        # 
        # By default, the historical scores that were generated in the seven days before the current date are queried.
        self.end_date = end_date
        # The region ID.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the YYYY-MM-DD format.
        # 
        # You can query the historical scores within the previous 180 days.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ListEvaluationScoreHistoryResponseBodyScoreHistoryTotalScoreHistory(TeaModel):
    def __init__(
        self,
        evaluation_time: str = None,
        score: float = None,
    ):
        # The time when the score was generated. The time is in UTC.
        self.evaluation_time = evaluation_time
        # The score.
        # 
        # Valid values: 0 to 1.
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_time is not None:
            result['EvaluationTime'] = self.evaluation_time
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationTime') is not None:
            self.evaluation_time = m.get('EvaluationTime')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class ListEvaluationScoreHistoryResponseBodyScoreHistory(TeaModel):
    def __init__(
        self,
        total_score_history: List[ListEvaluationScoreHistoryResponseBodyScoreHistoryTotalScoreHistory] = None,
    ):
        # The historical scores.
        self.total_score_history = total_score_history

    def validate(self):
        if self.total_score_history:
            for k in self.total_score_history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TotalScoreHistory'] = []
        if self.total_score_history is not None:
            for k in self.total_score_history:
                result['TotalScoreHistory'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.total_score_history = []
        if m.get('TotalScoreHistory') is not None:
            for k in m.get('TotalScoreHistory'):
                temp_model = ListEvaluationScoreHistoryResponseBodyScoreHistoryTotalScoreHistory()
                self.total_score_history.append(temp_model.from_map(k))
        return self


class ListEvaluationScoreHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        score_history: ListEvaluationScoreHistoryResponseBodyScoreHistory = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The historical scores.
        self.score_history = score_history

    def validate(self):
        if self.score_history:
            self.score_history.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.score_history is not None:
            result['ScoreHistory'] = self.score_history.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScoreHistory') is not None:
            temp_model = ListEvaluationScoreHistoryResponseBodyScoreHistory()
            self.score_history = temp_model.from_map(m['ScoreHistory'])
        return self


class ListEvaluationScoreHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEvaluationScoreHistoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEvaluationScoreHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunEvaluationRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        metric_ids: List[str] = None,
        region_id: str = None,
        scope: str = None,
    ):
        # The Alibaba Cloud account ID of the member. This parameter takes effect only when a multi-account governance maturity check is performed.
        self.account_id = account_id
        # The IDs of the check items to be checked.
        self.metric_ids = metric_ids
        # The region ID.
        self.region_id = region_id
        # The check range of the governance maturity check. Valid values:
        # 
        # *   Account (default): A single-account governance maturity check is performed to check only the Alibaba Cloud account that you use to access Cloud Governance Center.
        # *   ResourceDirectory: A multi-account governance maturity check is performed to check all members within a resource directory. Before you perform a multi-account governance maturity check, you must enable the multi-account governance maturity check feature.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.metric_ids is not None:
            result['MetricIds'] = self.metric_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('MetricIds') is not None:
            self.metric_ids = m.get('MetricIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class RunEvaluationShrinkRequest(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        metric_ids_shrink: str = None,
        region_id: str = None,
        scope: str = None,
    ):
        # The Alibaba Cloud account ID of the member. This parameter takes effect only when a multi-account governance maturity check is performed.
        self.account_id = account_id
        # The IDs of the check items to be checked.
        self.metric_ids_shrink = metric_ids_shrink
        # The region ID.
        self.region_id = region_id
        # The check range of the governance maturity check. Valid values:
        # 
        # *   Account (default): A single-account governance maturity check is performed to check only the Alibaba Cloud account that you use to access Cloud Governance Center.
        # *   ResourceDirectory: A multi-account governance maturity check is performed to check all members within a resource directory. Before you perform a multi-account governance maturity check, you must enable the multi-account governance maturity check feature.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.metric_ids_shrink is not None:
            result['MetricIds'] = self.metric_ids_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('MetricIds') is not None:
            self.metric_ids_shrink = m.get('MetricIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class RunEvaluationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunEvaluationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunEvaluationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunEvaluationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccountFactoryBaselineRequestBaselineItems(TeaModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        version: str = None,
    ):
        # The configurations of the baseline item. The value of this parameter is a JSON string.
        self.config = config
        # The name of the baseline item.
        self.name = name
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateAccountFactoryBaselineRequest(TeaModel):
    def __init__(
        self,
        baseline_id: str = None,
        baseline_items: List[UpdateAccountFactoryBaselineRequestBaselineItems] = None,
        baseline_name: str = None,
        description: str = None,
        region_id: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The baseline items.
        # 
        # You can call the [ListAccountFactoryBaselineItems](~~ListAccountFactoryBaselineItems~~) operation to query a list of baseline items supported by the account factory in Cloud Governance Center.
        self.baseline_items = baseline_items
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The description of the baseline.
        self.description = description
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.baseline_items:
            for k in self.baseline_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k in self.baseline_items:
                result['BaselineItems'].append(k.to_map() if k else None)
        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k in m.get('BaselineItems'):
                temp_model = UpdateAccountFactoryBaselineRequestBaselineItems()
                self.baseline_items.append(temp_model.from_map(k))
        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAccountFactoryBaselineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAccountFactoryBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAccountFactoryBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAccountFactoryBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


