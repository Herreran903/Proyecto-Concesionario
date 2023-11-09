import propTypes from "prop-types";
import React, {useState} from "react";
import VehicleContext from './VehicleContext';
import {checkVehicle} from "./VehicleValidation";
import {applySortFilter, getComparator} from "../filter/Filter";
import {getAllVehiculos, getVehiculo, createVehiculo, updateVehiculo} from "../../api/Vehiculo.api";
import {getAllModelos} from "../../api/Modelo.api";
import {getAllColors} from "../../api/Colors.api";
import { getAllEmpleados, getEmpleado, createEmpleado, updateEmpleado, deleteEmpleado } from "../../api/Empleado.api";
import { getAllSucursales, getSucursal } from "../../api/Sucursal.api";


VehicleState.propTypes = {
    children: propTypes.node,
}

export function VehicleState(props) {

    const TABLE_HEAD = [
        { id: 'vin', label: 'vin', alignRight: false },
        { id: 'modelo', label: 'modelo', alignRight: false },
        { id: 'sucursal', label: 'sucursal', alignRight: false },
        { id: 'color', label: 'color', alignRight: false },
        { id: '' },
    ];

    const emptyVehicle = {
        vin: "",
        modelo: "",
        sucursal: "",
        color: "",
    }
    const emptyError = {
        vin: "",
        modelo: "",
        sucursal: "",
        color: "",
    }

    const [vehicle, setVehicle] = React.useState(emptyVehicle);
    const [vehicles, setVehicles] = React.useState([]);
    const [openForm, setOpenForm] = useState(false);
    const [openDelete, setOpenDelete] = useState(false);
    const [openSnackbar, setOpenSnackbar] = useState(false);
    const [messageSnackbar, setMessageSnackbar] = useState('');
    const [typeSnackbar, setTypeSnackbar] = useState('success');
    const [models, setModels] = useState([]);
    const [colors, setColors] = useState([]);
    const [branches, setBranches] = useState([]);


    const getBranches = () => {
        async function loadBranches() {
            try{
                const response = await getAllSucursales();
                setBranches(response.data);
        
            } catch (error) {
                setTypeSnackbar('error');
                setMessageSnackbar('sucursales.mensaje.errorListando');
                handleOpenSnackbar();
            }
        }
        
        loadBranches();
    }

    const getColors = () => {
        async function loadColors() {
            try{
                const response = await getAllColors();
                setColors(response.data);
        
            } catch (error) {
                setTypeSnackbar('error');
                setMessageSnackbar('colores.mensaje.errorListando');
                handleOpenSnackbar();
            }
        }
        
        loadColors();
    }

    const getModels = () => {
        async function loadModels() {
            try{
                const response = await getAllModelos();
                setModels(response.data);
        
            } catch (error) {
                setTypeSnackbar('error');
                setMessageSnackbar('modelos.mensaje.errorListando');
                handleOpenSnackbar();
            }
        }
        
        loadModels();
    }


    const getVehicles = () => {
        async function loadVehicles() {
            try{
                const response = await getAllVehiculos();
                setVehicles(response.data);

            } catch (error) {
                setTypeSnackbar('error');
                setMessageSnackbar('empleados.mensaje.errorListando');
                handleOpenSnackbar();
            }
        }

        loadVehicles();        
    }

    const getVehicle = (vin) => {
        async function loadVehicles() {
            try{
                const response = await getVehiculo(vin);
                setVehicle(response.data);
            } catch (error) {
                setTypeSnackbar('error');
                setMessageSnackbar('vehiculos.mensaje.errorCargando');
                handleOpenSnackbar();
            }
        }

        if (vin === null) {
            setVehicle(emptyVehicle);
            setEdit(false);

        } else {
            loadVehicles();
            setEdit(true);
        }
    }

    const addVehicle = (vehicle) => {
        async function postVehicle() {
            try{
                const response = await createVehiculo(vehicle);
                setVehicles([...vehicles, response.data]);

                setTypeSnackbar('success');
                setMessageSnackbar('vehiculos.mensaje.agregado');
                handleOpenSnackbar();

                handleCloseForm();
            
            } catch (error) {
                const errors = error.response.data;

                if(errors.vin){
                    setTypeSnackbar('error');
                    setMessageSnackbar('vehiculos.mensaje.errorCedula');
                    setVehicleError({...vehicleError, vin: 'Vin ya existe'});
                    handleOpenSnackbar();

                } else {
                    setTypeSnackbar('error');
                    setMessageSnackbar('vehiculos.mensaje.error');
                    handleOpenSnackbar();
                }
            }
        }
        
        postVehicle();
    }

    const updateVehicle = (vehicle) => {
        async function putVehicle() {
            try{
                const response = await updateVehiculo(vehicle.vin, vehicle);
                setVehicles(vehicles.map((item) => (item.vin === vehicle.vin ? vehicle : item)));

                setTypeSnackbar('success');
                setMessageSnackbar('vehiculos.mensaje.editado');
                handleOpenSnackbar();

                handleCloseForm();
                getVehicles();
            
            } catch (error) {
                const errors = error.response.data;

                
            }
        }
        
        putVehicle();
    }

    const deleteVehicle = (vehicle) => {
        async function removeEmployee() {
            try{
                const response = await deleteEmpleado(vehicle.cedula);
                setVehicles(vehicles.filter((item) => item.cedula !== vehicle.cedula));

                setTypeSnackbar('success');
                setMessageSnackbar('empleados.mensaje.eliminado');
                handleOpenSnackbar();

                getVehicles();

            } catch (error) {
                const errors = error.response.data;

                if(errors.protected) {
                    setTypeSnackbar('error');
                    setMessageSnackbar(errors.protected);
                    handleOpenSnackbar();

                } else {
                    setTypeSnackbar('error');
                    setMessageSnackbar('empleados.mensaje.errorEliminar');
                    handleOpenSnackbar();
                }
            }
        }

        removeEmployee();
    }

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setVehicle({
            ...vehicle,
            [name]: value
        });
    }
    const handleSubmit = (event) => {
        event.preventDefault();
        if (!validateVehicleOnSubmit()) {
            if(edit)
            {
                updateVehicle(vehicle);
            }
            else
            {
                addVehicle(vehicle);
            }
            getVehicles();
        }
    }
    const handleOnBlur = (event) => {
        const {name} = event.target;
        validateVehicleOnBlur(vehicle, name);
    }

    const handleDelete = (event) => {
        event.preventDefault();
        deleteVehicle(vehicle);

        handleCloseDelete();
    }
    const handleOpenForm = (event, vin) => {
        getVehicleError();
        getBranches();
        getColors();
        getModels();
        getVehicle(vin);
        setOpenForm(true)
    };
    const handleCloseForm = () => {
        setOpenForm(false);
    };
    const handleOpenDelete = (event, vin) => {
        getVehicle(vin);
        setOpenDelete(true);
    }
    const handleCloseDelete = () => {
        setOpenDelete(false);
    }
    const handleCloseSnackbar = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setOpenSnackbar(false);
    }
    const handleOpenSnackbar = () => {
        setOpenSnackbar(true);
    }

    const [filterName, setFilterName] = useState('');
    const [order, setOrder] = useState('asc');
    const [orderBy, setOrderBy] = useState('vin');
    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(10);
    const [edit, setEdit] = React.useState(false);
    const [selected, setSelected] = React.useState([]);

    const handleRequestSort = (event, property) => {
        const isAsc = orderBy === property && order === 'asc';
        setOrder(isAsc ? 'desc' : 'asc');
        setOrderBy(property);
    };
    const handleClick = (event, name) => {
        const selectedIndex = selected.indexOf(name);
        let newSelected = [];
        if (selectedIndex === -1) {
            newSelected = newSelected.concat(selected, name);
        } else if (selectedIndex === 0) {
            newSelected = newSelected.concat(selected.slice(1));
        } else if (selectedIndex === selected.length - 1) {
            newSelected = newSelected.concat(selected.slice(0, -1));
        } else if (selectedIndex > 0) {
            newSelected = newSelected.concat(selected.slice(0, selectedIndex), selected.slice(selectedIndex + 1));
        }
        setSelected(newSelected);
    };
    const handleChangePage = (event, newPage) => {
        setPage(newPage);
    };
    const handleChangeRowsPerPage = (event) => {
        setPage(0);
        setRowsPerPage(parseInt(event.target.value, 10));
    };
    const handleFilterByName = (event) => {
        setPage(0);
        setFilterName(event.target.value);
    };

    const filteredVehicles = applySortFilter(vehicles, getComparator(order, orderBy), filterName);
    const emptyRows = page > 0 ? Math.max(0, (1 + page) * rowsPerPage - vehicles.length) : 0;
    const isNotFound = !filteredVehicles.length && !!filterName;

    const [vehicleError, setVehicleError] = React.useState(emptyError);

    const getVehicleError = () => {
        setVehicleError(emptyError)
    }

    const validateVehicleOnSubmit = () => {
        const updatedErrors = {};
        Object.keys(vehicleError).forEach((name) => {
            updatedErrors[name] = checkVehicle(vehicle, name);
        });
        setVehicleError(updatedErrors);
        return Object.values(updatedErrors).some((error) => error !== '');
    };
    const validateVehicleOnBlur = (vehicle, name) => {
        setVehicleError({...vehicleError, [name]: checkVehicle(vehicle, name)});
    };

    return (
        <VehicleContext.Provider value={
            {
                TABLE_HEAD,
                vehicle,
                vehicles,
                models,
                colors,
                branches,
                openForm,
                edit,
                openSnackbar,
                messageSnackbar,
                typeSnackbar,
                openDelete,
                getVehicles,
                getBranches,
                handleInputChange,
                handleSubmit,
                handleDelete,
                handleOnBlur,
                handleOpenForm,
                handleCloseForm,
                handleOpenDelete,
                handleCloseDelete,
                handleCloseSnackbar,
                filterName,
                order,
                orderBy,
                page,
                rowsPerPage,
                selected,
                filteredVehicles,
                emptyRows,
                isNotFound,
                handleRequestSort,
                handleClick,
                handleChangePage,
                handleChangeRowsPerPage,
                handleFilterByName,
                vehicleError,}}>
            {props.children}
        </VehicleContext.Provider>
    )
}



