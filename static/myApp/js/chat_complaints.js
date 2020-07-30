// JavaScript Document

$(function(){
	var myChart = echarts.init($(".line_char")[0]);
	option = {
		title: {
			text: '上两周投诉量情况'
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
				formatter: '{value} 次'
			}
		},
		series: [
			{
				name:'最高交易量',
				type:'line',
				data: [55, 34, 46, 54, 39, 207, 233, 187, 45, 33, 47, 39, 232, 221],
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
		text: '投诉类型占比图',
		x:'center'
	},
	tooltip : {
		trigger: 'item',
		formatter: "{a} <br/>{b} : {c} ({d}%)"
	},
	legend: {
		orient: 'vertical',
		x: 'left',
		data: ['卫生', '服务', '价格', '其他']
	},
	series : [
		{
			name: '酒店类型',
			type: 'pie',
			radius : '55%',
			center: ['50%', '60%'],
			data:[
				{ value: 1803, name: '卫生' },
				{ value: 1143, name: '服务' },
				{ value: 879, name: '价格' },
				{ value: 2134, name: '其他' }
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
            text: '投诉方式占比图',
            x: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            data: ['电话', '微信', '微博', '贴吧', '信件', '留言', '其他']
        },
        series: [
		{
		    name: '投诉方式',
		    type: 'pie',
		    radius: '55%',
		    center: ['50%', '60%'],
		    data: [
				{ value: 4255, name: '电话' },
				{ value: 2110, name: '微信' },
				{ value: 734, name: '微博' },
				{ value: 1125, name: '贴吧' },
				{ value: 1158, name: '信件' },
                { value: 335, name: '留言' },
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
