# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDtsInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_start: bool = None,
        compute_unit: int = None,
        database_count: int = None,
        destination_endpoint_engine_name: str = None,
        destination_region: str = None,
        dts_region: str = None,
        du: int = None,
        fee_type: str = None,
        insight_module: bool = None,
        instance_class: str = None,
        job_id: str = None,
        max_du: float = None,
        min_du: float = None,
        pay_type: str = None,
        period: str = None,
        quantity: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_endpoint_engine_name: str = None,
        source_region: str = None,
        sync_architecture: str = None,
        type: str = None,
        used_time: int = None,
    ):
        # Specifies whether to enable auto-renewal upon expiration. Valid values:
        # - **false**: no. This is the default value.
        # - **true**: yes.
        self.auto_pay = auto_pay
        # Specifies whether to automatically start the task after the purchase is completed. Valid values:
        # - **false**: no. This is the default value.
        # - **true**: yes.
        # 
        # > This parameter takes effect only when a valid task ID is specified for the **JobId** parameter and this parameter is set to **true**.
        self.auto_start = auto_start
        # The specifications of the ETL node. Unit: compute unit (CU). 1 CU equals 1 vCPU and 4 GB of memory. The value must be an integer greater than or equal to 2.
        # <props="china">
        # > If you specify this parameter, the [ETL feature](https://help.aliyun.com/document_detail/212324.html) is enabled to perform data cleaning and transformation.
        self.compute_unit = compute_unit
        # The number of private custom ApsaraDB RDS instances in PolarDB-X. Default value: **1**.
        # > This parameter is required only when the **SourceEndpointEngineName** parameter is set to **drds**.
        self.database_count = database_count
        # The database engine type of the destination instance. Valid values:
        # - **MySQL**: MySQL database, including ApsaraDB RDS for MySQL and self-managed MySQL databases.
        # - **PolarDB**: PolarDB for MySQL.
        # - **polardb_o**: PolarDB O DPI engine.
        # - **polardb_pg**: PolarDB for PostgreSQL.
        # - **Redis**: Redis database, including Tair (Redis OSS-Compatible) and self-managed Redis databases.
        # - **DRDS**: cloud-native distributed database PolarDB-X 1.0 and 2.0.
        # - **PostgreSQL**: self-managed PostgreSQL database.
        # - **odps**: MaxCompute.
        # - **oracle**: self-managed Oracle database.
        # - **mongodb**: MongoDB database, including ApsaraDB for MongoDB and self-managed MongoDB databases.
        # - **tidb**: TiDB database.
        # - **ADS**: cloud-native data warehouse AnalyticDB MySQL 2.0.
        # - **ADB30**: cloud-native data warehouse AnalyticDB MySQL 3.0.
        # - **Greenplum**: cloud-native data warehouse AnalyticDB PostgreSQL.
        # - **MSSQL**: SQL Server database, including ApsaraDB RDS for SQL Server and self-managed SQL Server databases.
        # - **kafka**: Kafka database, including MSMQ Kafka Edition and self-managed Kafka clusters.
        # - **DataHub**: DataHub.
        # - **DB2**: self-managed Db2 for LUW database.
        # - **as400**: AS/400.
        # - **Tablestore**: Tablestore.
        # 
        # > - Default value: **MySQL**.
        # - For more information about the supported source and destination databases, see [Supported databases, initial synchronization types, and synchronization topology](https://help.aliyun.com/document_detail/130744.html) and [Supported databases and migration types](https://help.aliyun.com/document_detail/26618.html).
        # - You must specify this parameter or the **JobId** parameter.
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        # The region of the destination instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > You must specify this parameter or the **JobId** parameter.
        self.destination_region = destination_region
        # The region to which the instance belongs. The value must be the same as the value of the **RegionId** parameter.
        self.dts_region = dts_region
        # The number of DUs allocated to the DTS task in the dedicated DTS cluster. Valid values: **1** to **100**.
        # 
        # >- The specified value must not exceed the number of available DUs in the dedicated DTS cluster.
        # - For more information about dedicated DTS clusters, see [What is a dedicated DTS cluster?](https://help.aliyun.com/document_detail/417481.html).
        self.du = du
        # The billing type for change tracking. Valid values:
        # - **ONLY_CONFIGURATION_FEE**: Only configuration fees are charged, and data traffic fees are waived.
        # - **CONFIGURATION_FEE_AND_DATA_FEE**: Data traffic fees are charged in addition to configuration fees.
        self.fee_type = fee_type
        self.insight_module = insight_module
        # The specifications of the data migration or data synchronization instance.
        # 
        # - Valid values for data migration instances: **xxlarge**, **xlarge**, **large**, **medium**, and **small**.
        # - Valid values for data synchronization instances: **large**, **medium**, **small**, and **micro**.
        # 
        # > For more information about the performance of different specifications, see [Specifications of data migration links](https://help.aliyun.com/document_detail/26606.html) and [Specifications of data synchronization links](https://help.aliyun.com/document_detail/26605.html).
        self.instance_class = instance_class
        # The task ID (**DtsJobId**) returned by the **ConfigureDtsJob** operation.
        # > If you specify this parameter, you do not need to specify the **SourceRegion**, **DestinationRegion**, **Type**, **SourceEndpointEngineName**, or **DestinationEndpointEngineName** parameters. Even if you specify them, the configurations in the **JobId** parameter prevail.
        self.job_id = job_id
        # The maximum number of DUs.
        # 
        # > This parameter is supported only for serverless instances.
        self.max_du = max_du
        # The minimum number of DUs.
        # 
        # > This parameter is supported only for serverless instances.
        self.min_du = min_du
        # The billing method. Valid values:
        # - **PrePaid**: subscription.
        # - **PostPaid**: pay-as-you-go.
        # 
        # > Note: This parameter is required.
        self.pay_type = pay_type
        # The billing method for a subscription instance. Valid values: **Year** and **Month**.
        # > This parameter is valid and required only when the **PayType** parameter is set to **PrePaid** (upfront).
        self.period = period
        # The number of instances that you want to purchase.
        # > You can purchase only one instance in a single call.
        self.quantity = quantity
        # The region of the instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The database engine type of the source instance. Valid values:
        # - **MySQL**: MySQL database, including ApsaraDB RDS for MySQL and self-managed MySQL databases.
        # - **PolarDB**: PolarDB for MySQL.
        # - **polardb_o**: PolarDB O DPI engine.
        # - **polardb_pg**: PolarDB for PostgreSQL.
        # - **Redis**: Redis database, including Tair (Redis OSS-Compatible) and self-managed Redis databases.
        # - **DRDS**: cloud-native distributed database PolarDB-X 1.0 and 2.0.
        # - **PostgreSQL**: self-managed PostgreSQL database.
        # - **odps**: MaxCompute.
        # - **oracle**: self-managed Oracle database.
        # - **mongodb**: MongoDB database, including ApsaraDB for MongoDB and self-managed MongoDB databases.
        # - **tidb**: TiDB database.
        # - **ADS**: cloud-native data warehouse AnalyticDB MySQL 2.0.
        # - **ADB30**: cloud-native data warehouse AnalyticDB MySQL 3.0.
        # - **Greenplum**: cloud-native data warehouse AnalyticDB PostgreSQL.
        # - **MSSQL**: SQL Server database, including ApsaraDB RDS for SQL Server and self-managed SQL Server databases.
        # - **kafka**: Kafka database, including MSMQ Kafka Edition and self-managed Kafka clusters.
        # - **DataHub**: DataHub.
        # - **DB2**: self-managed Db2 for LUW database.
        # - **as400**: AS/400.
        # - **Tablestore**: Tablestore.
        # - **OceanBase**: OceanBase (MySQL mode). Only data migration instances are supported.
        # 
        # > - Default value: **MySQL**.
        # - For more information about the supported source and destination databases, see [Supported databases, initial synchronization types, and synchronization topology](https://help.aliyun.com/document_detail/130744.html) and [Supported databases and migration types](https://help.aliyun.com/document_detail/26618.html).
        # - You must specify this parameter or the **JobId** parameter.
        self.source_endpoint_engine_name = source_endpoint_engine_name
        # The region of the source instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > You must specify this parameter or the **JobId** parameter.
        self.source_region = source_region
        # The synchronization topology. Valid values:
        # 
        # - **oneway**: one-way synchronization. This is the default value.
        # - **bidirectional**: two-way synchronization.
        self.sync_architecture = sync_architecture
        # The instance type. Valid values:
        # 
        # - **MIGRATION**: data migration.
        # - **SYNC**: data synchronization.
        # - **SUBSCRIBE**: change tracking.
        # > You must specify this parameter or the **JobId** parameter.
        self.type = type
        # The subscription duration of the instance.
        # - Valid values when the **Period** parameter is set to **Month**: 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        # - Valid values when the **Period** parameter is set to **Year**: 1, 2, 3, and 5.
        # > - This parameter is valid and required only when the **PayType** parameter is set to **PrePaid** (upfront).
        # - You can specify the billing method for the subscription instance in the **Period** parameter.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start

        if self.compute_unit is not None:
            result['ComputeUnit'] = self.compute_unit

        if self.database_count is not None:
            result['DatabaseCount'] = self.database_count

        if self.destination_endpoint_engine_name is not None:
            result['DestinationEndpointEngineName'] = self.destination_endpoint_engine_name

        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region

        if self.dts_region is not None:
            result['DtsRegion'] = self.dts_region

        if self.du is not None:
            result['Du'] = self.du

        if self.fee_type is not None:
            result['FeeType'] = self.fee_type

        if self.insight_module is not None:
            result['InsightModule'] = self.insight_module

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.max_du is not None:
            result['MaxDu'] = self.max_du

        if self.min_du is not None:
            result['MinDu'] = self.min_du

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.sync_architecture is not None:
            result['SyncArchitecture'] = self.sync_architecture

        if self.type is not None:
            result['Type'] = self.type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')

        if m.get('ComputeUnit') is not None:
            self.compute_unit = m.get('ComputeUnit')

        if m.get('DatabaseCount') is not None:
            self.database_count = m.get('DatabaseCount')

        if m.get('DestinationEndpointEngineName') is not None:
            self.destination_endpoint_engine_name = m.get('DestinationEndpointEngineName')

        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')

        if m.get('DtsRegion') is not None:
            self.dts_region = m.get('DtsRegion')

        if m.get('Du') is not None:
            self.du = m.get('Du')

        if m.get('FeeType') is not None:
            self.fee_type = m.get('FeeType')

        if m.get('InsightModule') is not None:
            self.insight_module = m.get('InsightModule')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MaxDu') is not None:
            self.max_du = m.get('MaxDu')

        if m.get('MinDu') is not None:
            self.min_du = m.get('MinDu')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('SyncArchitecture') is not None:
            self.sync_architecture = m.get('SyncArchitecture')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

