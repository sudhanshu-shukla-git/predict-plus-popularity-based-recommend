# predict-plus
## APIs

### Performance Based

#### https://predict-plus-recommender.herokuapp.com/performance_based

#### Sample Request : https://predict-plus-recommender.herokuapp.com/performance_based?mf_category=Debt%20Scheme&mf_sub_category=Liquid&risk=Moderate&top_n=5&load_cache=False
#### Method: GET
#### Allowed Values : 
#### Sample Result: 

```json
[{"1-Year Return(%)- Direct":"3.28","1-Year Return(%)- Regular":"3.21","3-Year Return(%)- Direct":"5.10","3-Year Return(%)- Regular":"5.04","5-Year Return(%)- Direct":"5.88","5-Year Return(%)- Regular":"5.81","benchmark":"NIFTY Liquid Fund Index","latest NAV- Direct":"2,325.0887","latest NAV- Regular":"2,311.9423","risk":"Moderate","scheme_name":"Axis Liquid Fund"},{"1-Year Return(%)- Direct":"3.25","1-Year Return(%)- Regular":"3.17","3-Year Return(%)- Direct":"4.98","3-Year Return(%)- Regular":"4.89","5-Year Return(%)- Direct":"5.80","5-Year Return(%)- Regular":"5.71","benchmark":"CRISIL Liquid Fund Index","latest NAV- Direct":"2,408.2207","latest NAV- Regular":"2,388.7586","risk":"Moderate","scheme_name":"BOI AXA Liquid Fund"},{"1-Year Return(%)- Direct":"3.42","1-Year Return(%)- Regular":"3.17","3-Year Return(%)- Direct":"5.19","3-Year Return(%)- Regular":"4.96","5-Year Return(%)- Direct":"5.89","5-Year Return(%)- Regular":"5.70","benchmark":"NIFTY Liquid Fund Index","latest NAV- Direct":"2,702.5092","latest NAV- Regular":"2,668.2378","risk":"Moderate","scheme_name":"Edelweiss Liquid Fund"},{"1-Year Return(%)- Direct":"3.23","1-Year Return(%)- Regular":"3.13","3-Year Return(%)- Direct":"5.01","3-Year Return(%)- Regular":"4.91","5-Year Return(%)- Direct":"5.76","5-Year Return(%)- Regular":"5.65","benchmark":"CRISIL Liquid Fund Index","latest NAV- Direct":"4,116.2249","latest NAV- Regular":"4,085.7339","risk":"Moderate","scheme_name":"HDFC Liquid Fund"},{"1-Year Return(%)- Direct":"2.93","1-Year Return(%)- Regular":"2.88","3-Year Return(%)- Direct":"4.41","3-Year Return(%)- Regular":"4.36","5-Year Return(%)- Direct":"5.25","5-Year Return(%)- Regular":"5.20","benchmark":"CRISIL Liquid Fund Index","latest NAV- Direct":"1,615.7312","latest NAV- Regular":"1,609.3442","risk":"Moderate","scheme_name":"IIFL Liquid Fund"}]
```

### Popularity Based

#### https://predict-plus-recommender.herokuapp.com/popularity_based

#### Sample Request : https://predict-plus-recommender.herokuapp.com/popularity_based?mf_category=Debt%20Scheme&mf_sub_category=Liquid&risk=Moderate&top_n=5&load_cache=False
#### Method: GET
#### Allowed Values : 
#### Sample Result: 

```json
[{"1-Year Return(%)- Direct":"4.21","1-Year Return(%)- Regular":"4.01","3-Year Return(%)- Direct":"4.56","3-Year Return(%)- Regular":"4.38","5-Year Return(%)- Direct":"5.22","5-Year Return(%)- Regular":"5.08","benchmark":"CRISIL Money Market Index","latest NAV- Direct":"3,750.6699","latest NAV- Regular":"3,716.5762","risk":"Moderate","scheme_name":"Tata Money Market Fund"},{"1-Year Return(%)- Direct":"3.23","1-Year Return(%)- Regular":"3.18","3-Year Return(%)- Direct":"5.02","3-Year Return(%)- Regular":"4.97","5-Year Return(%)- Direct":"5.81","5-Year Return(%)- Regular":"5.76","benchmark":"NIFTY Liquid Fund Index","latest NAV- Direct":"2,867.7412","latest NAV- Regular":"2,853.9973","risk":"Moderate","scheme_name":"L&T Liquid Fund"},{"1-Year Return(%)- Direct":"4.99","1-Year Return(%)- Regular":"3.91","3-Year Return(%)- Direct":"4.19","3-Year Return(%)- Regular":"3.16","5-Year Return(%)- Direct":"4.93","5-Year Return(%)- Regular":"3.92","benchmark":"CRISIL Short-Term Bond Index","latest NAV- Direct":"34.4743","latest NAV- Regular":"31.7902","risk":"Moderate","scheme_name":"HSBC Short Duration Fund"},{"1-Year Return(%)- Direct":"3.98","1-Year Return(%)- Regular":"2.82","3-Year Return(%)- Direct":"9.44","3-Year Return(%)- Regular":"8.28","5-Year Return(%)- Direct":"7.45","5-Year Return(%)- Regular":"6.41","benchmark":"CRISIL Composite Bond Index","latest NAV- Direct":"49.5722","latest NAV- Regular":"46.1093","risk":"Moderate","scheme_name":"Canara Robeco Income Fund"},{"1-Year Return(%)- Direct":"1.82","1-Year Return(%)- Regular":"1.04","3-Year Return(%)- Direct":"8.24","3-Year Return(%)- Regular":"7.39","5-Year Return(%)- Direct":"6.33","5-Year Return(%)- Regular":"5.51","benchmark":"CRISIL 10-Year Gilt","latest NAV- Direct":"2,428.4180","latest NAV- Regular":"2,258.8412","risk":"Moderate","scheme_name":"Invesco India Gilt Fund"}]
```
