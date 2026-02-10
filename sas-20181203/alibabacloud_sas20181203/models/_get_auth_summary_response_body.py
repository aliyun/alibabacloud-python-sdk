# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetAuthSummaryResponseBody(DaraModel):
    def __init__(
        self,
        allow_partial_buy: int = None,
        allow_upgrade_partial_buy: int = None,
        allow_user_unbind: int = None,
        auto_bind: int = None,
        cluster_node_check: int = None,
        default_auth_to_all: int = None,
        has_pre_bind_setting: bool = None,
        highest_version: int = None,
        invalid_bind_status: str = None,
        is_multi_version: int = None,
        machine: main_models.GetAuthSummaryResponseBodyMachine = None,
        post_paid_highest_version: str = None,
        post_paid_host_auto_bind: str = None,
        post_paid_host_auto_bind_version: str = None,
        post_paid_version_summary: List[main_models.GetAuthSummaryResponseBodyPostPaidVersionSummary] = None,
        request_id: str = None,
        version_summary: List[main_models.GetAuthSummaryResponseBodyVersionSummary] = None,
    ):
        # Indicates whether you can purchase protection quota on demand when you purchase Security Center. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.allow_partial_buy = allow_partial_buy
        # Indicates whether you can purchase protection quota on demand after an upgrade. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.allow_upgrade_partial_buy = allow_upgrade_partial_buy
        # Indicates whether all bound assets can be immediately unbound. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.allow_user_unbind = allow_user_unbind
        # Indicates whether automatic binding is enabled. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.auto_bind = auto_bind
        # Cluster node need to check the machine version,  Value:
        # 
        # - **0** : Not required
        # 
        # - **1** : Required
        self.cluster_node_check = cluster_node_check
        # Indicates whether the protection quota is supported for all assets. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.default_auth_to_all = default_auth_to_all
        # Indicates whether pre-bound assets exist. If you select assets to bind when you purchase Security Center, pre-bound assets exist. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.has_pre_bind_setting = has_pre_bind_setting
        # The most advanced edition that is used. Valid values:
        # 
        # *   **1**: Basic edition
        # *   **3**: Enterprise edition
        # *   **5**: Advanced edition
        # *   **6**: Anti-virus edition
        # *   **7**: Ultimate edition
        # *   **10**: Value-added Plan edition
        # 
        # >  If you purchase Security Center Multi-edition, the value indicates the most advanced edition that is used. Otherwise, the value indicates the specific edition that is purchased.
        self.highest_version = highest_version
        # Binding effective status, value:
        # 
        # - **NORMAL** : Effective
        # 
        # - **INVALID_NODE_VERSION**: Invalid
        self.invalid_bind_status = invalid_bind_status
        # Indicates whether Security Center Multi-edition is purchased. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.is_multi_version = is_multi_version
        # The statistics of the protection quota for assets.
        self.machine = machine
        # Activate the pay-as-you-go service protection version for hosts and container security, which is the highest protection version among all bound hosts. Values:   - **1**: Free Edition  - **3**: Enterprise Edition - **5**: Advanced Edition - **6**: Antivirus Edition     - **7**: Flagship Edition
        self.post_paid_highest_version = post_paid_highest_version
        # The pay-as-you-go service for host and container security adds an automatic binding identifier for new hosts, with values: - **0**: Off - **1**: On
        self.post_paid_host_auto_bind = post_paid_host_auto_bind
        # The version for the pay-as-you-go service of host and container security to automatically bind new assets, with values: - **1**: Free Edition - **3**: Enterprise Edition - **5**: Advanced Edition - **6**: Antivirus Edition - **7**: Flagship Edition
        self.post_paid_host_auto_bind_version = post_paid_host_auto_bind_version
        # Statistics on pay-as-you-go service authorization for host and container security.
        self.post_paid_version_summary = post_paid_version_summary
        # The request ID.
        self.request_id = request_id
        # The quota consumption statistics.
        self.version_summary = version_summary

    def validate(self):
        if self.machine:
            self.machine.validate()
        if self.post_paid_version_summary:
            for v1 in self.post_paid_version_summary:
                 if v1:
                    v1.validate()
        if self.version_summary:
            for v1 in self.version_summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_partial_buy is not None:
            result['AllowPartialBuy'] = self.allow_partial_buy

        if self.allow_upgrade_partial_buy is not None:
            result['AllowUpgradePartialBuy'] = self.allow_upgrade_partial_buy

        if self.allow_user_unbind is not None:
            result['AllowUserUnbind'] = self.allow_user_unbind

        if self.auto_bind is not None:
            result['AutoBind'] = self.auto_bind

        if self.cluster_node_check is not None:
            result['ClusterNodeCheck'] = self.cluster_node_check

        if self.default_auth_to_all is not None:
            result['DefaultAuthToAll'] = self.default_auth_to_all

        if self.has_pre_bind_setting is not None:
            result['HasPreBindSetting'] = self.has_pre_bind_setting

        if self.highest_version is not None:
            result['HighestVersion'] = self.highest_version

        if self.invalid_bind_status is not None:
            result['InvalidBindStatus'] = self.invalid_bind_status

        if self.is_multi_version is not None:
            result['IsMultiVersion'] = self.is_multi_version

        if self.machine is not None:
            result['Machine'] = self.machine.to_map()

        if self.post_paid_highest_version is not None:
            result['PostPaidHighestVersion'] = self.post_paid_highest_version

        if self.post_paid_host_auto_bind is not None:
            result['PostPaidHostAutoBind'] = self.post_paid_host_auto_bind

        if self.post_paid_host_auto_bind_version is not None:
            result['PostPaidHostAutoBindVersion'] = self.post_paid_host_auto_bind_version

        result['PostPaidVersionSummary'] = []
        if self.post_paid_version_summary is not None:
            for k1 in self.post_paid_version_summary:
                result['PostPaidVersionSummary'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VersionSummary'] = []
        if self.version_summary is not None:
            for k1 in self.version_summary:
                result['VersionSummary'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPartialBuy') is not None:
            self.allow_partial_buy = m.get('AllowPartialBuy')

        if m.get('AllowUpgradePartialBuy') is not None:
            self.allow_upgrade_partial_buy = m.get('AllowUpgradePartialBuy')

        if m.get('AllowUserUnbind') is not None:
            self.allow_user_unbind = m.get('AllowUserUnbind')

        if m.get('AutoBind') is not None:
            self.auto_bind = m.get('AutoBind')

        if m.get('ClusterNodeCheck') is not None:
            self.cluster_node_check = m.get('ClusterNodeCheck')

        if m.get('DefaultAuthToAll') is not None:
            self.default_auth_to_all = m.get('DefaultAuthToAll')

        if m.get('HasPreBindSetting') is not None:
            self.has_pre_bind_setting = m.get('HasPreBindSetting')

        if m.get('HighestVersion') is not None:
            self.highest_version = m.get('HighestVersion')

        if m.get('InvalidBindStatus') is not None:
            self.invalid_bind_status = m.get('InvalidBindStatus')

        if m.get('IsMultiVersion') is not None:
            self.is_multi_version = m.get('IsMultiVersion')

        if m.get('Machine') is not None:
            temp_model = main_models.GetAuthSummaryResponseBodyMachine()
            self.machine = temp_model.from_map(m.get('Machine'))

        if m.get('PostPaidHighestVersion') is not None:
            self.post_paid_highest_version = m.get('PostPaidHighestVersion')

        if m.get('PostPaidHostAutoBind') is not None:
            self.post_paid_host_auto_bind = m.get('PostPaidHostAutoBind')

        if m.get('PostPaidHostAutoBindVersion') is not None:
            self.post_paid_host_auto_bind_version = m.get('PostPaidHostAutoBindVersion')

        self.post_paid_version_summary = []
        if m.get('PostPaidVersionSummary') is not None:
            for k1 in m.get('PostPaidVersionSummary'):
                temp_model = main_models.GetAuthSummaryResponseBodyPostPaidVersionSummary()
                self.post_paid_version_summary.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.version_summary = []
        if m.get('VersionSummary') is not None:
            for k1 in m.get('VersionSummary'):
                temp_model = main_models.GetAuthSummaryResponseBodyVersionSummary()
                self.version_summary.append(temp_model.from_map(k1))

        return self

class GetAuthSummaryResponseBodyVersionSummary(DaraModel):
    def __init__(
        self,
        auth_bind_type: str = None,
        index: int = None,
        total_core_auth_count: int = None,
        total_count: int = None,
        total_ecs_auth_count: int = None,
        un_used_count: int = None,
        unused_core_auth_count: int = None,
        unused_ecs_auth_count: int = None,
        used_core_count: int = None,
        used_ecs_count: int = None,
        version: int = None,
    ):
        # The type of the quota that is consumed. Valid values:
        # 
        # *   ASSET: quota of servers.
        # *   CORE: quota of server cores.
        # *   ASSET_AND_CORE: both.
        self.auth_bind_type = auth_bind_type
        # The index of the current edition. The smaller the value, the higher the edition. The index is used for sorting.
        self.index = index
        # The total quota of server cores.
        # 
        # >  This parameter takes effect only if AuthBindType is set to CORE or ASSET_AND_CORE.
        self.total_core_auth_count = total_core_auth_count
        # The total quota of servers in the current edition.
        # 
        # >  This parameter takes effect only if AuthBindType is set to ASSET or ASSET_AND_CORE.
        self.total_count = total_count
        # The total quota of servers.
        # 
        # >  This parameter takes effect only if AuthBindType is set to ASSET or ASSET_AND_CORE.
        self.total_ecs_auth_count = total_ecs_auth_count
        # The remaining quota of servers.
        # 
        # >  This parameter takes effect only if AuthBindType is set to ASSET or ASSET_AND_CORE.
        self.un_used_count = un_used_count
        # The remaining quota of server cores.
        # 
        # >  This parameter takes effect only if AuthBindType is set to CORE or ASSET_AND_CORE.
        self.unused_core_auth_count = unused_core_auth_count
        # The remaining quota of servers.
        # 
        # >  This parameter takes effect only if AuthBindType is set to ASSET or ASSET_AND_CORE.
        self.unused_ecs_auth_count = unused_ecs_auth_count
        # The consumed quota of server cores.
        # 
        # >  This parameter takes effect only if AuthBindType is set to CORE or ASSET_AND_CORE.
        self.used_core_count = used_core_count
        # The used quota of servers.
        # 
        # >  This parameter takes effect only if AuthBindType is set to ASSET or ASSET_AND_CORE.
        self.used_ecs_count = used_ecs_count
        # The edition of purchased Security Center. Valid values:
        # 
        # *   **1**: Basic edition
        # *   **3**: Enterprise edition
        # *   **5**: Advanced edition
        # *   **6**: Anti-virus edition
        # *   **7**: Ultimate edition
        # *   **8**: Multi-edition
        # *   **10**: Value-added Plan edition
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_bind_type is not None:
            result['AuthBindType'] = self.auth_bind_type

        if self.index is not None:
            result['Index'] = self.index

        if self.total_core_auth_count is not None:
            result['TotalCoreAuthCount'] = self.total_core_auth_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_ecs_auth_count is not None:
            result['TotalEcsAuthCount'] = self.total_ecs_auth_count

        if self.un_used_count is not None:
            result['UnUsedCount'] = self.un_used_count

        if self.unused_core_auth_count is not None:
            result['UnusedCoreAuthCount'] = self.unused_core_auth_count

        if self.unused_ecs_auth_count is not None:
            result['UnusedEcsAuthCount'] = self.unused_ecs_auth_count

        if self.used_core_count is not None:
            result['UsedCoreCount'] = self.used_core_count

        if self.used_ecs_count is not None:
            result['UsedEcsCount'] = self.used_ecs_count

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthBindType') is not None:
            self.auth_bind_type = m.get('AuthBindType')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('TotalCoreAuthCount') is not None:
            self.total_core_auth_count = m.get('TotalCoreAuthCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalEcsAuthCount') is not None:
            self.total_ecs_auth_count = m.get('TotalEcsAuthCount')

        if m.get('UnUsedCount') is not None:
            self.un_used_count = m.get('UnUsedCount')

        if m.get('UnusedCoreAuthCount') is not None:
            self.unused_core_auth_count = m.get('UnusedCoreAuthCount')

        if m.get('UnusedEcsAuthCount') is not None:
            self.unused_ecs_auth_count = m.get('UnusedEcsAuthCount')

        if m.get('UsedCoreCount') is not None:
            self.used_core_count = m.get('UsedCoreCount')

        if m.get('UsedEcsCount') is not None:
            self.used_ecs_count = m.get('UsedEcsCount')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetAuthSummaryResponseBodyPostPaidVersionSummary(DaraModel):
    def __init__(
        self,
        auth_bind_type: str = None,
        index: int = None,
        used_core_count: int = None,
        used_ecs_count: int = None,
        version: int = None,
    ):
        # The type of authorization consumed during binding, with values: - **ASSET**: Consumes the number of authorized devices - **CORE**: Consumes the number of authorized cores - **ASSET_AND_CORE**: Consumes both the number of authorized devices and cores.
        self.auth_bind_type = auth_bind_type
        # Current version index, the higher the number, the newer the version, used for sorting. Values: - **1**: Free Edition - **2**: Anti-virus Edition - **3**: Advanced Edition - **4**: Enterprise Edition - **5**: Flagship Edition
        self.index = index
        # Number of authorized cores used. > This parameter is valid when AuthBindType is set to CORE or ASSET_AND_CORE.
        self.used_core_count = used_core_count
        # Number of authorized devices used. > This parameter is valid when AuthBindType is ASSET or ASSET_AND_CORE.
        self.used_ecs_count = used_ecs_count
        # Bound host assets with postpaid versions, values:   - **1**: Free version  - **3**: Enterprise version - **5**: Advanced version - **6**: Anti-virus version     - **7**: Flagship version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_bind_type is not None:
            result['AuthBindType'] = self.auth_bind_type

        if self.index is not None:
            result['Index'] = self.index

        if self.used_core_count is not None:
            result['UsedCoreCount'] = self.used_core_count

        if self.used_ecs_count is not None:
            result['UsedEcsCount'] = self.used_ecs_count

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthBindType') is not None:
            self.auth_bind_type = m.get('AuthBindType')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('UsedCoreCount') is not None:
            self.used_core_count = m.get('UsedCoreCount')

        if m.get('UsedEcsCount') is not None:
            self.used_ecs_count = m.get('UsedEcsCount')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetAuthSummaryResponseBodyMachine(DaraModel):
    def __init__(
        self,
        bind_core_count: int = None,
        bind_ecs_count: int = None,
        post_paid_bind_core_count: int = None,
        post_paid_bind_ecs_count: int = None,
        risk_core_count: int = None,
        risk_ecs_count: int = None,
        total_core_count: int = None,
        total_ecs_count: int = None,
        un_bind_core_count: int = None,
        un_bind_ecs_count: int = None,
    ):
        # The number of cores of the assets that are bound to Security Center.
        self.bind_core_count = bind_core_count
        # The number of the assets that are bound to Security Center.
        self.bind_ecs_count = bind_ecs_count
        # Bind the number of cores for postpaid authorization assets.
        self.post_paid_bind_core_count = post_paid_bind_core_count
        # The number of assets bound to the postpaid authorization.
        self.post_paid_bind_ecs_count = post_paid_bind_ecs_count
        # The number of cores of the assets that are at risk.
        self.risk_core_count = risk_core_count
        # The number of the assets that are at risk.
        self.risk_ecs_count = risk_ecs_count
        # The total number of asset cores.
        self.total_core_count = total_core_count
        # The total number of assets.
        self.total_ecs_count = total_ecs_count
        # The number of cores of unbound assets.
        self.un_bind_core_count = un_bind_core_count
        # The number of unbound assets.
        self.un_bind_ecs_count = un_bind_ecs_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_core_count is not None:
            result['BindCoreCount'] = self.bind_core_count

        if self.bind_ecs_count is not None:
            result['BindEcsCount'] = self.bind_ecs_count

        if self.post_paid_bind_core_count is not None:
            result['PostPaidBindCoreCount'] = self.post_paid_bind_core_count

        if self.post_paid_bind_ecs_count is not None:
            result['PostPaidBindEcsCount'] = self.post_paid_bind_ecs_count

        if self.risk_core_count is not None:
            result['RiskCoreCount'] = self.risk_core_count

        if self.risk_ecs_count is not None:
            result['RiskEcsCount'] = self.risk_ecs_count

        if self.total_core_count is not None:
            result['TotalCoreCount'] = self.total_core_count

        if self.total_ecs_count is not None:
            result['TotalEcsCount'] = self.total_ecs_count

        if self.un_bind_core_count is not None:
            result['UnBindCoreCount'] = self.un_bind_core_count

        if self.un_bind_ecs_count is not None:
            result['UnBindEcsCount'] = self.un_bind_ecs_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindCoreCount') is not None:
            self.bind_core_count = m.get('BindCoreCount')

        if m.get('BindEcsCount') is not None:
            self.bind_ecs_count = m.get('BindEcsCount')

        if m.get('PostPaidBindCoreCount') is not None:
            self.post_paid_bind_core_count = m.get('PostPaidBindCoreCount')

        if m.get('PostPaidBindEcsCount') is not None:
            self.post_paid_bind_ecs_count = m.get('PostPaidBindEcsCount')

        if m.get('RiskCoreCount') is not None:
            self.risk_core_count = m.get('RiskCoreCount')

        if m.get('RiskEcsCount') is not None:
            self.risk_ecs_count = m.get('RiskEcsCount')

        if m.get('TotalCoreCount') is not None:
            self.total_core_count = m.get('TotalCoreCount')

        if m.get('TotalEcsCount') is not None:
            self.total_ecs_count = m.get('TotalEcsCount')

        if m.get('UnBindCoreCount') is not None:
            self.un_bind_core_count = m.get('UnBindCoreCount')

        if m.get('UnBindEcsCount') is not None:
            self.un_bind_ecs_count = m.get('UnBindEcsCount')

        return self

