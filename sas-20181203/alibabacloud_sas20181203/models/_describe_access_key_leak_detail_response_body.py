# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccessKeyLeakDetailResponseBody(DaraModel):
    def __init__(
        self,
        accesskey_id: str = None,
        asset: str = None,
        code: str = None,
        deal_time: str = None,
        deal_type: str = None,
        github_file_name: str = None,
        github_file_type: str = None,
        github_file_update_time: str = None,
        github_file_url: str = None,
        github_repo_name: str = None,
        github_repo_url: str = None,
        github_user: str = None,
        github_user_pic_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        remark: str = None,
        request_id: str = None,
        source: str = None,
        token_valid: int = None,
        type: str = None,
        whitelist_status: str = None,
        whitelist_time: int = None,
    ):
        # The ID of the AccessKey pair that is leaked.
        self.accesskey_id = accesskey_id
        # The platform to which the asset belongs. The value is fixed as **Cloud platform**.
        self.asset = asset
        # The code snippet that is leaked.
        self.code = code
        # The time when the AccessKey pair leak was handled.
        self.deal_time = deal_time
        # The solution to the AccessKey pair leak. Valid values:
        # 
        # *   **manual**: manually deleted
        # *   **disable**: manually disabled
        # *   **add-whitelist**: added to the whitelist
        # *   **pending**: unhandled
        self.deal_type = deal_type
        # The name of the GitHub file.
        self.github_file_name = github_file_name
        # The type of the GitHub file. Valid values:
        # 
        # *   Python
        # *   XML
        # *   GO
        # *   Javascript
        # *   INI
        # *   JSON
        # *   C++
        self.github_file_type = github_file_type
        # The time when the GitHub file was updated.
        self.github_file_update_time = github_file_update_time
        # The URL of the GitHub file.
        self.github_file_url = github_file_url
        # The name of the GitHub repository.
        self.github_repo_name = github_repo_name
        # The URL of the GitHub repository.
        self.github_repo_url = github_repo_url
        # The username of the GitHub user.
        self.github_user = github_user
        # The URL of the profile picture for the GitHub user.
        self.github_user_pic_url = github_user_pic_url
        # The first time when the AccessKey pair leak was detected.
        self.gmt_create = gmt_create
        # The last time when the AccessKey pair leak was detected.
        self.gmt_modified = gmt_modified
        # The remarks of the AccessKey pair leak.
        self.remark = remark
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The platform on which the AccessKey pair leak is detected.
        self.source = source
        # The validity of the key that is associated with the AccessKey pair. Valid values:
        # 
        # *   **0**: to be confirmed.
        # *   **1**: valid.
        # *   **2**: invalid.
        self.token_valid = token_valid
        # The type of the leak. The value is fixed as **AccessKey**.
        self.type = type
        # Indicates whether the AccessKey pair leak is added to the whitelist. Valid values:
        # 
        # *   **no**: no
        # *   **yes**: yes
        self.whitelist_status = whitelist_status
        # The time when the AccessKey pair was added to the whitelist. Unit: milliseconds.
        self.whitelist_time = whitelist_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accesskey_id is not None:
            result['AccesskeyId'] = self.accesskey_id

        if self.asset is not None:
            result['Asset'] = self.asset

        if self.code is not None:
            result['Code'] = self.code

        if self.deal_time is not None:
            result['DealTime'] = self.deal_time

        if self.deal_type is not None:
            result['DealType'] = self.deal_type

        if self.github_file_name is not None:
            result['GithubFileName'] = self.github_file_name

        if self.github_file_type is not None:
            result['GithubFileType'] = self.github_file_type

        if self.github_file_update_time is not None:
            result['GithubFileUpdateTime'] = self.github_file_update_time

        if self.github_file_url is not None:
            result['GithubFileUrl'] = self.github_file_url

        if self.github_repo_name is not None:
            result['GithubRepoName'] = self.github_repo_name

        if self.github_repo_url is not None:
            result['GithubRepoUrl'] = self.github_repo_url

        if self.github_user is not None:
            result['GithubUser'] = self.github_user

        if self.github_user_pic_url is not None:
            result['GithubUserPicUrl'] = self.github_user_pic_url

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source is not None:
            result['Source'] = self.source

        if self.token_valid is not None:
            result['TokenValid'] = self.token_valid

        if self.type is not None:
            result['Type'] = self.type

        if self.whitelist_status is not None:
            result['WhitelistStatus'] = self.whitelist_status

        if self.whitelist_time is not None:
            result['WhitelistTime'] = self.whitelist_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccesskeyId') is not None:
            self.accesskey_id = m.get('AccesskeyId')

        if m.get('Asset') is not None:
            self.asset = m.get('Asset')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')

        if m.get('DealType') is not None:
            self.deal_type = m.get('DealType')

        if m.get('GithubFileName') is not None:
            self.github_file_name = m.get('GithubFileName')

        if m.get('GithubFileType') is not None:
            self.github_file_type = m.get('GithubFileType')

        if m.get('GithubFileUpdateTime') is not None:
            self.github_file_update_time = m.get('GithubFileUpdateTime')

        if m.get('GithubFileUrl') is not None:
            self.github_file_url = m.get('GithubFileUrl')

        if m.get('GithubRepoName') is not None:
            self.github_repo_name = m.get('GithubRepoName')

        if m.get('GithubRepoUrl') is not None:
            self.github_repo_url = m.get('GithubRepoUrl')

        if m.get('GithubUser') is not None:
            self.github_user = m.get('GithubUser')

        if m.get('GithubUserPicUrl') is not None:
            self.github_user_pic_url = m.get('GithubUserPicUrl')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TokenValid') is not None:
            self.token_valid = m.get('TokenValid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WhitelistStatus') is not None:
            self.whitelist_status = m.get('WhitelistStatus')

        if m.get('WhitelistTime') is not None:
            self.whitelist_time = m.get('WhitelistTime')

        return self

