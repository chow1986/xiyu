// JavaScript Document

$(function(){
	var myChart = echarts.init($(".line_char")[0]);
	option = {
		title: {
			text: '上两周交易量情况'
		},
		tooltip: {
			trigger: 'axis'
		},
		toolbox: {
			show: true,
			feature: {
				dataZoom: {
					yAxisIndex: 'none'
				},
				dataView: {readOnly: false},
				magicType: {type: ['line', 'bar']},
				restore: {},
				saveAsImage: {}
			}
		},
		xAxis:  {
			type: 'category',
			boundaryGap: false,
			data: ['2016.09.26', '2016.09.27', '2016.09.28', '2016.09.29', '2016.09.30', '2016.10.1', '2016.10.2', '2016.10.3', '2016.10.4', '2016.10.5', '2016.10.6', '2016.10.7', '2016.10.8', '2016.10.9']
		},
		yAxis: {
			type: 'value',
			axisLabel: {
				formatter: '{value} 元'
			}
		},
		series: [
			{
				name:'最高交易量',
				type:'line',
				data: [65753, 67548, 98352, 88042, 127482, 135435, 105643, 65753, 67548, 98352, 88042, 127482, 135435, 105643],
				markPoint: {
					data: [
						{type: 'max', name: '最大值'},
						{type: 'min', name: '最小值'}
					]
				},
				markLine: {
					data: [
						{type: 'average', name: '平均值'}
					]
				}
			}
		]
	};
	myChart.setOption(option);
});

$(function(){
	var myChart = echarts.init($(".pie_char")[0]);
option = {
	title : {
		text: '入住酒店类型占比图',
		x:'center'
	},
	tooltip : {
		trigger: 'item',
		formatter: "{a} <br/>{b} : {c} ({d}%)"
	},
	legend: {
		orient: 'vertical',
		x: 'left',
		data: ['五星级', '四星级', '三星级', '二星级', '一星级', '快捷酒店', '商务酒店', '其他']
	},
	series : [
		{
			name: '酒店类型',
			type: 'pie',
			radius : '55%',
			center: ['50%', '60%'],
			data:[
				{ value: 255, name: '五星级' },
				{ value: 2110, name: '四星级' },
				{ value: 3234, name: '三星级' },
				{ value: 1125, name: '二星级' },
				{ value: 158, name: '一星级' },
                { value: 5335, name: '快捷酒店' },
				{ value: 7110, name: '商务酒店' },
				{ value: 4634, name: '其他' }
			],
			itemStyle: {
				emphasis: {
					shadowBlur: 10,
					shadowOffsetX: 0,
					shadowColor: 'rgba(0, 0, 0, 0.5)'
				}
			}
		}
	]
};myChart.setOption(option);
});

$(function () {
    var myChart = echarts.init($("#pie_char1")[0]);
    option = {
        title: {
            text: '入住房间类型占比图',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            data: ['单人间', '标准间', '套房', '豪华单人间', '豪华标准间', '豪华套房', '其他']
        },
        series: [
		{
		    name: '酒店类型',
		    type: 'pie',
		    radius: '55%',
		    center: ['50%', '60%'],
		    data: [
				{ value: 4255, name: '单人间' },
				{ value: 2110, name: '标准间' },
				{ value: 734, name: '套房' },
				{ value: 1125, name: '豪华单人间' },
				{ value: 1158, name: '豪华标准间' },
                { value: 335, name: '豪华套房' },
				{ value: 634, name: '其他' }
			],
		    itemStyle: {
		        emphasis: {
		            shadowBlur: 10,
		            shadowOffsetX: 0,
		            shadowColor: 'rgba(0, 0, 0, 0.5)'
		        }
		    }
		}
	]
    }; myChart.setOption(option);
});
